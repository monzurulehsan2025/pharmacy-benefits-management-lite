from fastapi.testclient import TestClient
from main import app
import pytest
import time

client = TestClient(app)

def test_get_member_profile_found():
    """Test retrieving a valid member profile."""
    response = client.get("/api/v1/members/MEM-992834")
    assert response.status_code == 200
    data = response.json()
    assert data["member_id"] == "MEM-992834"
    assert data["first_name"] == "Sarah"
    assert "active_medications" in data

def test_get_member_profile_not_found():
    """Test retrieving a non-existent member profile."""
    response = client.get("/api/v1/members/MEM-UNKNOWN")
    assert response.status_code == 404
    assert response.json()["detail"] == "Member not found"

def test_process_claim_success():
    """Test processing a pharmacy claim."""
    claim_data = {
        "member_id": "MEM-992834",
        "npi_id": "1234567890",
        "ndc_code": "0002-3227-30",
        "quantity": 30,
        "days_supply": 30
    }
    response = client.post("/api/v1/claims/process", json=claim_data)
    assert response.status_code == 201
    data = response.json()
    assert "claim_id" in data
    assert data["status"] == "APPROVED"
    assert data["total_cost"] == 45.00

def test_get_drug_pricing_success():
    """Test retrieving drug pricing options."""
    response = client.get("/api/v1/drugs/pricing?drug_name=Lipitor&zip_code=10001&quantity=30")
    assert response.status_code == 200
    data = response.json()
    assert "Lipitor" in data["drug_name"]
    assert len(data["options"]) > 0
    assert data["options"][0]["pharmacy"] == "CVS Health"

def test_update_care_plan_success():
    """Test updating a member care plan."""
    plan_data = {
        "intervention_strategy": "Increase adherence monitoring",
        "goals": ["Improve PDC score to > 0.80", "Reduce out-of-pocket costs"],
        "assigned_pharmacist": "Dr. James Wilson"
    }
    response = client.put("/api/v1/members/MEM-992834/care-plan", json=plan_data)
    assert response.status_code == 200
    data = response.json()
    assert data["member_id"] == "MEM-992834"
    assert data["status"] == "UPDATED"
    assert "revision_id" in data

def test_get_medication_adherence_success_v2():
    """Test retrieving medication adherence metrics for the 11th API."""
    response = client.get("/api/v1/clinical/adherence/MEM-992834")
    assert response.status_code == 200
    data = response.json()
    assert data["member_id"] == "MEM-992834"
    assert "overall_adherence_score" in data
    assert len(data["medications"]) == 2
    assert data["medications"][0]["name"] == "Metformin"
    assert data["medications"][0]["status"] == "ADHERENT"
    assert "recommendation" in data

def test_get_member_profile_latency():
    """Test that retrieving a member profile is within acceptable latency limits."""
    start_time = time.time()
    response = client.get("/api/v1/members/MEM-992834")
    end_time = time.time()
    latency = end_time - start_time
    assert response.status_code == 200
    assert latency < 0.2, f"Latency too high: {latency}s"

def test_process_claim_latency():
    """Test that processing a claim is within acceptable latency limits."""
    claim_data = {
        "member_id": "MEM-992834",
        "npi_id": "1234567890",
        "ndc_code": "0002-3227-30",
        "quantity": 30,
        "days_supply": 30
    }
    start_time = time.time()
    response = client.post("/api/v1/claims/process", json=claim_data)
    end_time = time.time()
    latency = end_time - start_time
    assert response.status_code == 201
    assert latency < 0.3, f"Latency too high: {latency}s"
