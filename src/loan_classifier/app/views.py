# app/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import numpy as np
import json
from .utils import model  # Ensure this is importing your trained model

@csrf_exempt
def predict_credit_score(request):
    if request.method == 'POST':
        try:
            # Define the feature order for the input data (should be 46 features)
            feature_order = [
                "month", "age", "annual_income", "monthly_inhand_salary", 
                "total_emi_per_month", "num_bank_accounts", "num_credit_card", 
                "interest_rate", "num_of_loan", "delay_from_due_date", 
                "num_of_delayed_payment", "changed_credit_limit", 
                "num_credit_inquiries", "credit_mix", "outstanding_debt", 
                "credit_utilization_ratio", "credit_history_age", 
                "payment_of_min_amount", "amount_invested_monthly", 
                "payment_behaviour", "monthly_balance",  
                "auto_loan", "credit_builder_loan", "debt_consolidation_loan", 
                "home_equity_loan", "mortgage_loan", "no_loan", 
                "not_specified", "payday_loan", "personal_loan", 
                "student_loan", "occupation_Accountant", "occupation_Architect", 
                "occupation_Developer", "occupation_Doctor", "occupation_Engineer", 
                "occupation_Entrepreneur", "occupation_Journalist", "occupation_Lawyer", 
                "occupation_Manager", "occupation_Mechanic", "occupation_Media_Manager", 
                "occupation_Musician", "occupation_Scientist", "occupation_Teacher", 
                "occupation_Writer"
            ]

            # Parse JSON input from request body
            data = json.loads(request.body)

            # Encode categorical features to numeric values
            credit_mix_mapping = {
                "Standard": 1,
                "Good": 2,
                "Bad": 0
            }

            payment_of_min_amount_mapping = {
                "Yes": 1,
                "No": 0
            }

            # Map the input features
            data['credit_mix'] = credit_mix_mapping.get(data.get('credit_mix'), 0)  # Default to 0 if invalid value
            data['payment_of_min_amount'] = payment_of_min_amount_mapping.get(data.get('payment_of_min_amount'), 0)  # Default to 0 if invalid value

            # Check if only one occupation and one loan type are set to 1
            loan_features = ["auto_loan", "credit_builder_loan", "debt_consolidation_loan", 
                             "home_equity_loan", "mortgage_loan", "no_loan", "payday_loan", 
                             "personal_loan", "student_loan"]
            occupation_features = [
                "occupation_Accountant", "occupation_Architect", "occupation_Developer", 
                "occupation_Doctor", "occupation_Engineer", "occupation_Entrepreneur", 
                "occupation_Journalist", "occupation_Lawyer", "occupation_Manager", 
                "occupation_Mechanic", "occupation_Media_Manager", "occupation_Musician", 
                "occupation_Scientist", "occupation_Teacher", "occupation_Writer"
            ]

            # Check if exactly one loan type and one occupation are selected
            loan_count = sum([data.get(loan, 0) for loan in loan_features])
            occupation_count = sum([data.get(occupation, 0) for occupation in occupation_features])

            if loan_count != 1:
                return JsonResponse({"error": "Exactly one loan type should be selected."}, status=400)
            if occupation_count != 1:
                return JsonResponse({"error": "Exactly one occupation should be selected."}, status=400)

            # Prepare the input data for prediction
            input_data = np.array([data.get(feature, 0) for feature in feature_order]).reshape(1, -1)

            # Ensure the input matches the expected shape
            if input_data.shape[1] != 46:
                return JsonResponse({"error": "Incorrect number of features. Expected 46."}, status=400)

            # Make prediction using the pre-loaded model
            predictions = model.predict(input_data)
            predicted_class = predictions.argmax(axis=1)[0]  # Class with the highest probability

            # Map the predicted class to credit score
            credit_score_mapping = {
                0: "Poor",  # Class 0: Poor
                1: "Standard",  # Class 1: Standard
                2: "Good"  # Class 2: Good
            }

            # Return prediction as JSON response
            return JsonResponse({"credit_score": credit_score_mapping.get(predicted_class, "Unknown")})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"message": "Only POST requests are allowed."}, status=405)
