# insurance_logic.py

"""
Spartacus Dental AI Assistant
Rule-based insurance estimate logic.

This version does NOT use Vertex AI or an API key.
It gives a realistic educational simulation based on procedure codes.
"""


PROCEDURE_RULES = {
    "D1110": {
        "name": "Adult Cleaning",
        "category": "Preventive",
        "coverage": "80% - 100%",
        "approval": "High",
        "notes": "Usually covered as preventive care. Frequency limits may apply."
    },
    "D0120": {
        "name": "Periodic Oral Evaluation",
        "category": "Preventive",
        "coverage": "80% - 100%",
        "approval": "High",
        "notes": "Often covered every 6 months depending on the insurance plan."
    },
    "D2391": {
        "name": "Tooth-Colored Filling",
        "category": "Basic Restorative",
        "coverage": "50% - 80%",
        "approval": "Medium to High",
        "notes": "Coverage may depend on tooth location and plan limitations."
    },
    "D2740": {
        "name": "Porcelain Crown",
        "category": "Major Restorative",
        "coverage": "40% - 60%",
        "approval": "Medium",
        "notes": "Pre-authorization is often recommended. Documentation and X-rays may be required."
    },
    "D7210": {
        "name": "Surgical Tooth Extraction",
        "category": "Oral Surgery",
        "coverage": "50% - 80%",
        "approval": "Medium",
        "notes": "Coverage depends on medical necessity and supporting documentation."
    },
    "D8080": {
        "name": "Comprehensive Orthodontic Treatment",
        "category": "Orthodontics",
        "coverage": "Limited or Plan-Specific",
        "approval": "Low to Medium",
        "notes": "Many plans have lifetime orthodontic maximums or age restrictions."
    }
}


def analyze_procedure(procedure_code, insurance_provider):
    """
    Analyze a dental procedure code and return estimated insurance information.
    """

    code = procedure_code.strip().upper()
    provider = insurance_provider.strip().title()

    if code in PROCEDURE_RULES:
        result = PROCEDURE_RULES[code]

        return {
            "procedure_code": code,
            "procedure_name": result["name"],
            "insurance_provider": provider if provider else "Not provided",
            "category": result["category"],
            "estimated_coverage": result["coverage"],
            "approval_likelihood": result["approval"],
            "notes": result["notes"],
            "disclaimer": "This is an educational estimate only and not a real insurance determination."
        }

    return {
        "procedure_code": code,
        "procedure_name": "Unknown procedure code",
        "insurance_provider": provider if provider else "Not provided",
        "category": "Unknown",
        "estimated_coverage": "Unable to estimate",
        "approval_likelihood": "Unknown",
        "notes": "This procedure code is not currently in the demo database. Add it to PROCEDURE_RULES to expand the system.",
        "disclaimer": "This is an educational estimate only and not a real insurance determination."
    }
