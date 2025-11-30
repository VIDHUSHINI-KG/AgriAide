ADVICE_DB = {
    "healthy": "Plant is healthy. Continue routine irrigation.",
    "leaf_rust": "Use copper fungicide. Remove affected leaves.",
    "late_blight": "Remove affected plants. Apply approved fungicide.",
    "powdery_mildew": "Use sulfur spray. Improve aeration.",
    "bacterial_spot": "Avoid overhead irrigation. Use disease-free seeds."
}

def get_advice(recommendation_id):
    key = recommendation_id.lower()
    return ADVICE_DB.get(key, "No precise advice found.")
