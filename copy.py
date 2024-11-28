# import shutil

# # Path to the original notebook
# original_notebook_path = "notebooks/feature_selection.ipynb"

# # Path to the new notebook (can be a different directory or name)
# new_notebook_path = "model_training.ipynb"

# # Copy the notebook
# shutil.copy(original_notebook_path, new_notebook_path)


import numpy as np
from tensorflow.models import load_model
import pandas as pd

# Charger le modèle Keras
model = load_model('100k_ann_model.keras')

# Données d'entrée (comme vous l'avez fourni)
input_data = {
    "month": [1],
    "age": [23],
    "annual_income": [19114.843],
    "monthly_inhand_salary": [1824.843],
    "total_emi_per_month": [49.575],
    "num_bank_accounts": [3],
    "num_credit_card": [4],
    "interest_rate": [3],  
    "num_of_loan": [4],  
    "delay_from_due_date": [3],
    "num_of_delayed_payment": [7], 
    "changed_credit_limit": [11.270],
    "num_credit_inquiries": [4],  
    "credit_mix": ['Good'],  # Note: should be numerically encoded if needed
    "outstanding_debt": [809.980],  
    "credit_utilization_ratio": [26.823], 
    "credit_history_age": [265],  
    "payment_of_min_amount": ['No'],  # Note: should be numerically encoded if needed
    "amount_invested_monthly": [80.415],
    "payment_behaviour": [4],
    "monthly_balance": [312.494],  
    "auto_loan": [1],
    "credit_builder_loan": [1],
    "debt_consolidation_loan": [0],
    "home_equity_loan": [1],
    "mortgage_loan": [0],
    "no_loan": [0],
    "not_specified": [0],
    "payday_loan": [0],
    "personal_loan": [1],
    "student_loan": [0],
    "occupation_Accountant": [0],
    "occupation_Architect": [0],
    "occupation_Developer": [0],
    "occupation_Doctor": [0],
    "occupation_Engineer": [0],
    "occupation_Entrepreneur": [0],
    "occupation_Journalist": [0],
    "occupation_Lawyer": [0],
    "occupation_Manager": [0],
    "occupation_Mechanic": [0],
    "occupation_Media_Manager": [0],
    "occupation_Musician": [0],
    "occupation_Scientist": [1],
    "occupation_Teacher": [0],
    "occupation_Writer": [0]
}

# Convertir les données d'entrée en DataFrame
input_df = pd.DataFrame(input_data)

# Encoder les variables catégorielles (si nécessaire)
# Par exemple, pour 'credit_mix' et 'payment_of_min_amount', vous pouvez les encoder
input_df['credit_mix'] = input_df['credit_mix'].map({'Good': 1, 'Standard': 0})
input_df['payment_of_min_amount'] = input_df['payment_of_min_amount'].map({'Yes': 1, 'No': 0})

# Vous devrez peut-être effectuer d'autres transformations sur les données selon la manière dont elles ont été prétraitées pendant l'entraînement.

# Faire une prédiction avec le modèle
predictions = model.predict(input_df)

# Afficher les probabilités pour chaque classe
# Si votre modèle fait une classification binaire ou multiclasse, vous obtiendrez une probabilité par classe
# Exemple pour classification binaire :
if predictions.shape[1] == 2:
    print(f"Probabilité de la classe 'Good' : {predictions[0][0]}")
    print(f"Probabilité de la classe 'Standard' : {predictions[0][1]}")
    predicted_class = 'Good' if predictions[0][0] > predictions[0][1] else 'Standard'

# Si c'est une classification multi-classe, adaptez selon les sorties de votre modèle
else:
    print(f"Probabilités des classes : {predictions[0]}")

# Afficher la classe prédite
print(f"Classe prédite : {predicted_class}")
