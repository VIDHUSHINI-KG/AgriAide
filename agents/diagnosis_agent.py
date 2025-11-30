import random

def diagnose_leaf(image_path):
    possible = [
        ("Healthy", 0.92),
        ("Leaf Rust", 0.78),
        ("Late Blight", 0.68),
        ("Powdery Mildew", 0.74),
        ("Bacterial Spot", 0.63)
    ]
    disease, conf = random.choice(possible)
    return {
        "disease": disease,
        "confidence": round(conf, 2),
        "recommendation_id": disease.replace(" ", "_").lower()
    }
