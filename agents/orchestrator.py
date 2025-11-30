from .diagnosis_agent import diagnose_leaf
from .advisory_agent import get_advice
from .marketplace_agent import get_suppliers
from .memory import log_interaction, get_user

def run_pipeline(user_id, image_path):
    diag = diagnose_leaf(image_path)
    advice = get_advice(diag["recommendation_id"])
    suppliers = get_suppliers(diag["recommendation_id"])

    result = {
        "diagnosis": diag,
        "advice": advice,
        "suppliers": suppliers
    }

    log_interaction(user_id, "diagnosis", str(result))
    return result
