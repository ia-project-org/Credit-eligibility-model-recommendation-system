from tensorflow.keras.models import load_model
import joblib



scaler = joblib.load(r'C:\Users\chaym\OneDrive - Université Cadi Ayyad Marrakech\Documents\CI5\INTELLIGENCE ARTIFICIELLE\Credit_eligibility_AI_recommendation_system\src\loan_classifier\ml\scaler.pkl')
model = load_model(r"C:\Users\chaym\OneDrive - Université Cadi Ayyad Marrakech\Documents\CI5\INTELLIGENCE ARTIFICIELLE\Credit_eligibility_AI_recommendation_system\src\loan_classifier\ml\100k_ann_model.keras")
print("Model loaded successfully:", model)

