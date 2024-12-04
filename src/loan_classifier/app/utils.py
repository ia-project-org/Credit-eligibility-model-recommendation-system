from tensorflow.keras.models import load_model

#model = load_model("../ml/100k_ann_model.keras")
model = load_model(r"D:\Credit_eligibility_AI_recommendation_system-main\Credit_eligibility_AI_recommendation_system-main\src\loan_classifier\ml\100k_ann_model.keras")
print("Model loaded successfully:", model)
