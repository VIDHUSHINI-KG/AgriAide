SUPPLIERS = {
    "leaf_rust": ["Local Agri Store A", "Village Co-op Center"],
    "late_blight": ["GreenGrow Fertilizers", "HarvestPoint Agro"],
    "powdery_mildew": ["EcoFarm Inputs", "Agricare Shop"],
    "bacterial_spot": ["Krishi Seva Kendra", "Farmers Mart"]
}

def get_suppliers(recommendation_id):
    return SUPPLIERS.get(recommendation_id.lower(), ["No local suppliers found"])
