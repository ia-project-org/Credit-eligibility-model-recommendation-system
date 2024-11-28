# app/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .utils import model  
from .utils import scaler
import pandas as pd
import numpy as np

@csrf_exempt
def predict_credit_score(request):
    if request.method == 'POST':
        try:
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

            data = json.loads(request.body)

            credit_mix_mapping = {
                "Standard": 1,
                "Good": 2,
                "Bad": 0
            }

            payment_of_min_amount_mapping = {
                "Yes": 1,
                "No": 0
            }

            data['credit_mix'] = credit_mix_mapping.get(data.get('credit_mix'), 0)
            data['payment_of_min_amount'] = payment_of_min_amount_mapping.get(data.get('payment_of_min_amount'), 0) 

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

            occupation_count = sum([data.get(occupation, 0) for occupation in occupation_features])

            if not any(data.get(loan, 0) for loan in loan_features):
                return JsonResponse({"error": "At least one loan type must be selected."}, status=400)

            if occupation_count != 1:
                return JsonResponse({"error": "Exactly one occupation should be selected."}, status=400)

            input_data = pd.DataFrame([data], columns=feature_order)

            input_scaled = scaler.transform(input_data)

            predictions = model.predict(input_scaled)
            predicted_class = predictions.argmax(axis=1)[0]  

            credit_score_mapping = {
                0: "Poor",  
                1: "Standard",  
                2: "Good" 
            }

            return JsonResponse({"credit_score": credit_score_mapping.get(predicted_class, "Unknown")})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"message": "Only POST requests are allowed."}, status=405)
