# HealthStack Solutions Clinical API Backend

This is a professional-grade Python backend implementation for HealthStack Solutions. The system focuses on pharmacy benefits management (PBM), clinical outcomes optimization, and engineering management transparency.

## 🚀 Overview

The backend is built using **FastAPI**, providing high performance, data validation through **Pydantic**, and automatic interactive documentation.

### Key Features
- **10 RESTful Endpoints**: Covering members, claims, AI clinical insights, FHIR interoperability, and engineering KPIs.
- **Realistic Mock Data**: Concrete, realistic responses for pharmacy benefits and clinical healthcare scenarios.
- **Modern Architecture**: Ready for event-driven integration and microservices.
- **Auto-Documentation**: Interactive Swagger and ReDoc interfaces.

## 🛠️ Technology Stack
- **Language**: Python 3.10+
- **Framework**: FastAPI
- **Validation**: Pydantic
- **Execution**: Uvicorn

## 📋 API Documentation

### 1. Get Member Clinical Profile
**Endpoint**: `GET /api/v1/members/{member_id}`
**Description**: Retrieves the clinical history and demographic information for a specific health plan member.

**Sample Request**:
```json
{
  "path_params": {
    "member_id": "MEM-992834"
  }
}
```

**Sample Response**:
```json
{
  "member_id": "MEM-992834",
  "first_name": "Sarah",
  "last_name": "Chen",
  "dob": "1982-05-14",
  "risk_score": 0.82,
  "conditions": ["Type 2 Diabetes", "Hypertension"],
  "active_medications": [
    {"name": "Metformin", "dosage": "500mg", "frequency": "Daily"},
    {"name": "Lisinopril", "dosage": "10mg", "frequency": "Daily"}
  ]
}
```

---

### 2. Process Pharmacy Claim
**Endpoint**: `POST /api/v1/claims/process`
**Description**: Submits a real-time pharmacy claim for adjudication and cost calculation.

**Sample Request**:
```json
{
  "member_id": "MEM-992834",
  "npi_id": "1234567890",
  "ndc_code": "00002-8244-01",
  "quantity": 30,
  "days_supply": 30
}
```

**Sample Response**:
```json
{
  "claim_id": "CLM-55021",
  "status": "APPROVED",
  "total_cost": 45.00,
  "member_responsibility": 10.00,
  "plan_responsibility": 35.00,
  "adjudication_timestamp": "2024-05-20T14:30:00Z"
}
```

---

### 3. Get AI Clinical Insights
**Endpoint**: `GET /api/v1/clinical/insights/{member_id}`
**Description**: Fetches AI-driven clinical recommendations from the CarePath AI platform to improve health outcomes.

**Sample Request**:
```json
{
  "path_params": {
    "member_id": "MEM-992834"
  }
}
```

**Sample Response**:
```json
{
  "member_id": "MEM-992834",
  "insights": [
    {
      "type": "THERAPY_OPTIMIZATION",
      "confidence": 0.94,
      "recommendation": "Switch to generic Metformin Extended Release to improve adherence and reduce cost.",
      "estimated_annual_savings": 240.00
    },
    {
      "type": "ADHERENCE_RISK",
      "confidence": 0.88,
      "recommendation": "Member missed last two refills of Lisinopril. High risk of cardiovascular event.",
      "priority": "HIGH"
    }
  ]
}
```

---

### 4. Drug Pricing Search
**Endpoint**: `GET /api/v1/drugs/pricing`
**Description**: Retrieves real-time pricing for a drug across different pharmacy networks for cost transparency.

**Sample Request**:
```bash
GET /api/v1/drugs/pricing?drug_name=Lipitor&zip_code=10001&quantity=30
```

**Sample Response**:
```json
{
  "drug_name": "Lipitor (Atorvastatin)",
  "options": [
    {"pharmacy": "CVS Health", "price": 12.50, "distance_miles": 0.5},
    {"pharmacy": "Walgreens", "price": 14.00, "distance_miles": 1.2},
    {"pharmacy": "Costco Pharmacy", "price": 8.75, "distance_miles": 3.5}
  ]
}
```

---

### 5. Submit Prior Authorization
**Endpoint**: `POST /api/v1/prior-authorization/request`
**Description**: Initiates a prior authorization request for high-cost or specialty medications.

**Sample Request**:
```json
{
  "member_id": "MEM-992834",
  "prescriber_id": "PRV-112233",
  "drug_name": "Humira",
  "diagnosis_code": "M06.9",
  "supporting_notes": "Patient failed first-line therapy with methotrexate."
}
```

**Sample Response**:
```json
{
  "request_id": "PA-778844",
  "status": "PENDING_REVIEW",
  "estimated_turnaround": "24 hours",
  "submission_id": "SUB-99110"
}
```

---

### 6. Member Cohort Health Analytics
**Endpoint**: `GET /api/v1/analytics/cohort-health`
**Description**: Provides aggregate clinical health data for a sponsor's specific member cohort.

**Sample Request**:
```bash
GET /api/v1/analytics/cohort-health?group_id=GRP-HEALTHSTACK-TECH&metric=HbA1c_control
```

**Sample Response**:
```json
{
  "group_id": "GRP-HEALTHSTACK-TECH",
  "metric": "HbA1c_control",
  "period": "Q1 2024",
  "results": {
    "total_members": 500,
    "controlled_percentage": 74.5,
    "improvement_from_prev_quarter": "+3.2%",
    "top_interventions": ["Medication Therapy Management", "Digital Coaching"]
  }
}
```

---

### 7. FHIR Patient Resource
**Endpoint**: `GET /api/v1/integrations/fhir/Patient/{member_id}`
**Description**: Retrieves member data in HL7 FHIR R4 format for interoperability with other health systems.

**Sample Response**:
```json
{
  "resourceType": "Patient",
  "id": "MEM-992834",
  "identifier": [
    { "system": "https://healthstack.io/member-ids", "value": "992834" }
  ],
  "name": [{ "family": "Chen", "given": ["Sarah"] }],
  "gender": "female",
  "birthDate": "1982-05-14"
}
```

---

### 8. Trigger Clinical Alert
**Endpoint**: `POST /api/v1/messages/clinical-alert`
**Description**: Sends a critical clinical alert via event-driven messaging (Kafka/Azure Service Bus).

**Sample Request**:
```json
{
  "member_id": "MEM-992834",
  "alert_type": "DRUG_DRUG_INTERACTION",
  "severity": "CRITICAL",
  "message": "Potential interaction between newly prescribed Warfarin and existing Amiodarone."
}
```

**Sample Response**:
```json
{
  "alert_id": "ALT-123",
  "delivery_status": "QUEUED",
  "channels": ["SMS", "PROVIDER_PORTAL"],
  "event_ref": "evt_9988776655"
}
```

---

### 9. Get Delivery KPIs
**Endpoint**: `GET /api/v1/system/delivery-kpis`
**Description**: Retrieves engineering performance metrics for management review.

**Sample Response**:
```json
{
  "teams": [
    {
      "name": "Clinical AI Team",
      "sprint_velocity": 42,
      "bug_count": 3,
      "deployment_frequency": "Daily",
      "uptime": "99.99%"
    },
    {
      "name": "Claims Core Team",
      "sprint_velocity": 38,
      "bug_count": 5,
      "deployment_frequency": "Weekly",
      "uptime": "99.95%"
    }
  ]
}
```

---

### 10. Update Member Care Plan
**Endpoint**: `PUT /api/v1/members/{member_id}/care-plan`
**Description**: Updates a member's clinical goals and intervention strategy.

**Sample Request**:
```json
{
  "intervention_strategy": "AGGRESSIVE_ADHERENCE",
  "goals": ["Lower HbA1c below 7.0", "Reduce daily pill burden"],
  "assigned_pharmacist": "Dr. Robert Smith"
}
```

**Sample Response**:
```json
{
  "member_id": "MEM-992834",
  "status": "UPDATED",
  "revision_id": "REV-104",
  "last_updated": "2024-05-20T16:00:00Z"
}
```

---

### 11. Get Medication Adherence Metrics
**Endpoint**: `GET /api/v1/clinical/adherence/{member_id}`
**Description**: Calculates Proportion of Days Covered (PDC) and identifies gaps in medication therapy.

**Sample Request**:
```json
{
  "path_params": {
    "member_id": "MEM-992834"
  }
}
```

**Sample Response**:
```json
{
  "member_id": "MEM-992834",
  "overall_adherence_score": 0.88,
  "medications": [
    {
      "name": "Metformin",
      "pdc_score": 0.92,
      "status": "ADHERENT",
      "last_fill_date": "2024-05-01",
      "days_since_last_fill": 19
    },
    {
      "name": "Lisinopril",
      "pdc_score": 0.75,
      "status": "NON_ADHERENT",
      "last_fill_date": "2024-04-10",
      "days_since_last_fill": 40
    }
  ],
  "recommendation": "High risk for Lisinopril gap. Initiate automated refill reminder."
}
```

## 🏃 Getting Started

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Server**:
   ```bash
   python main.py
   ```

3. **Access Documentation**:
   - Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
   - ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## 📂 Data Definition
The formal API definitions and concrete examples can be found in `api_definitions.json`.
