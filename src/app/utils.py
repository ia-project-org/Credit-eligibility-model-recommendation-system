from tensorflow.keras.models import load_model
import joblib



scaler = joblib.load(r'./ml/scaler.pkl')
model = load_model(r'./ml/100k_ann_model.keras')
print("Model loaded successfully:", model)
