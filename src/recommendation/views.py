# from django.shortcuts import render
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.core.mail import send_mail
# import json

# # Constants for occupations
# HIGH_INCOME_OCCUPATIONS = ['Lawyer', 'Engineer', 'Architect', 'Scientist', 'Accountant', 'Developer', 'Manager']
# LOW_INCOME_OCCUPATIONS = ['Teacher', 'Musician', 'Writer', 'Journalist']

# # Loan recommendation functions
# def recommend_auto_loan(client):
#     if ((20 <= client.get('age', 0) <= 60 and
#          client.get('annual_income', 0) > 30000 and
#          client.get('credit_mix') in ['Good', 'Excellent'] and
#          client.get('payment_behaviour') in ['High_spent_Large_value_payments', 'High_spent_Medium_value_payments']) or
#         ('Auto Loan' not in client.get('type_of_loan', []) and client.get('occupation') in HIGH_INCOME_OCCUPATIONS)):
#         return True
#     return False

# def recommend_credit_builder_loan(client):
#     if ((client.get('age', 0) < 35 and
#          client.get('annual_income', 0) > 10000 and
#          client.get('payment_behaviour') in ['Low_spent_Small_value_payments', 'Low_spent_Medium_value_payments']) or
#         ('Credit-Builder Loan' not in client.get('type_of_loan', [])) or
#         (client.get('occupation') in LOW_INCOME_OCCUPATIONS)):
#         return True
#     return False

# def recommend_home_equity_loan(client):
#     if ((client.get('monthly_balance', 0) > 2000 and
#          client.get('credit_history_age', 0) > 5) or
#         ('Home Equity Loan' not in client.get('type_of_loan', [])) or
#         (client.get('occupation') in HIGH_INCOME_OCCUPATIONS)):
#         return True
#     return False

# def recommend_mortgage_loan(client):
#     if ((25 <= client.get('age', 0) <= 60 and
#          client.get('annual_income', 0) > 50000) or
#         ('Mortgage Loan' not in client.get('type_of_loan', [])) or
#         (client.get('occupation') in HIGH_INCOME_OCCUPATIONS)):
#         return True
#     return False

# def recommend_payday_loan(client):
#     if (client.get('payment_behaviour') == 'Low_spent_Small_value_payments' or
#         'Payday Loan' not in client.get('type_of_loan', [])):
#         return True
#     return False

# def recommend_student_loan(client):
#     if ((client.get('age', 0) < 30 and client.get('annual_income', 0) < 30000) or
#         'Student Loan' not in client.get('type_of_loan', [])):
#         return True
#     return False

# # Main loan recommendation function
# def loan_recommendation(client):
#     recommendations = {}
#     if recommend_auto_loan(client):
#         recommendations['Auto Loan'] = True
#     if recommend_credit_builder_loan(client):
#         recommendations['Credit-Builder Loan'] = True
#     if recommend_home_equity_loan(client):
#         recommendations['Home Equity Loan'] = True
#     if recommend_mortgage_loan(client):
#         recommendations['Mortgage Loan'] = True
#     if recommend_payday_loan(client):
#         recommendations['Payday Loan'] = True
#     if recommend_student_loan(client):
#         recommendations['Student Loan'] = True
#     return recommendations

# # Django view to handle recommendations and send emails
# @csrf_exempt
# def recommend_and_email(request):
#     if request.method == "POST":
#         try:
#             client_data = json.loads(request.body)

#             # Validate email
#             email = client_data.get('email')
#             if not email:
#                 return JsonResponse({"status": "error", "message": "Email is required."})

#             recommendations = loan_recommendation(client_data)

#             subject = "Your Loan Recommendations"
#             message = f"Dear {client_data.get('name', 'Client')},\n\nBased on your financial profile, we recommend the following loan(s):\n\n"
#             for loan, recommend in recommendations.items():
#                 if recommend:
#                     message += f"- {loan}\n"
#             message += "\nThank you for choosing our services!"

#             # Send email
#             send_mail(
#                 subject,
#                 message,
#                 "smartcredit.supp@gmail.com",  
#                 [email],   
#                 fail_silently=False,
#             )

#             return JsonResponse({"status": "success", "message": "Recommendations sent via email!", "recommendations": recommendations})
#         except Exception as e:
#             return JsonResponse({"status": "error", "message": str(e)})

#     return JsonResponse({"status": "error", "message": "Invalid request method."})


from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
import json

# Constants for occupations
HIGH_INCOME_OCCUPATIONS = ['Lawyer', 'Engineer', 'Architect', 'Scientist', 'Accountant', 'Developer', 'Manager']
LOW_INCOME_OCCUPATIONS = ['Teacher', 'Musician', 'Writer', 'Journalist']

# Loan recommendation functions
def recommend_auto_loan(client):
    if ((20 <= client.get('age', 0) <= 60 and
         client.get('annual_income', 0) > 30000 and
         client.get('credit_mix') in ['Good', 'Excellent'] and
         client.get('payment_behaviour') in ['High_spent_Large_value_payments', 'High_spent_Medium_value_payments']) or
        ('Auto Loan' not in client.get('type_of_loan', []) and client.get('occupation') in HIGH_INCOME_OCCUPATIONS)):
        return True
    return False

def recommend_credit_builder_loan(client):
    if ((client.get('age', 0) < 35 and
         client.get('annual_income', 0) > 10000 and
         client.get('payment_behaviour') in ['Low_spent_Small_value_payments', 'Low_spent_Medium_value_payments']) or
        ('Credit-Builder Loan' not in client.get('type_of_loan', [])) or
        (client.get('occupation') in LOW_INCOME_OCCUPATIONS)):
        return True
    return False

def recommend_home_equity_loan(client):
    if ((client.get('monthly_balance', 0) > 2000 and
         client.get('credit_history_age', 0) > 5) or
        ('Home Equity Loan' not in client.get('type_of_loan', [])) or
        (client.get('occupation') in HIGH_INCOME_OCCUPATIONS)):
        return True
    return False

def recommend_mortgage_loan(client):
    if ((25 <= client.get('age', 0) <= 60 and
         client.get('annual_income', 0) > 50000) or
        ('Mortgage Loan' not in client.get('type_of_loan', [])) or
        (client.get('occupation') in HIGH_INCOME_OCCUPATIONS)):
        return True
    return False

def recommend_payday_loan(client):
    if (client.get('payment_behaviour') == 'Low_spent_Small_value_payments' or
        'Payday Loan' not in client.get('type_of_loan', [])):
        return True
    return False

def recommend_student_loan(client):
    if ((client.get('age', 0) < 30 and client.get('annual_income', 0) < 30000) or
        'Student Loan' not in client.get('type_of_loan', [])):
        return True
    return False

# Main loan recommendation function
def loan_recommendation(client):
    recommendations = {}
    if recommend_auto_loan(client):
        recommendations['Auto Loan'] = True
    if recommend_credit_builder_loan(client):
        recommendations['Credit-Builder Loan'] = True
    if recommend_home_equity_loan(client):
        recommendations['Home Equity Loan'] = True
    if recommend_mortgage_loan(client):
        recommendations['Mortgage Loan'] = True
    if recommend_payday_loan(client):
        recommendations['Payday Loan'] = True
    if recommend_student_loan(client):
        recommendations['Student Loan'] = True
    return recommendations

# Django view to handle recommendations and send bold, compact emails
@csrf_exempt
def recommend_and_email(request):
    if request.method == "POST":
        try:
            client_data = json.loads(request.body)

            # Validate email
            email = client_data.get('email')
            if not email:
                return JsonResponse({"status": "error", "message": "Email is required."})

            recommendations = loan_recommendation(client_data)

            # Email subject
            subject = "🚗📚 Your Next Loan Adventure Awaits! 🏡💰"

            # HTML and bold formatted email message
            loan_messages = {
                'Auto Loan': f"""
                    <p><strong>Hey {client_data.get('name', 'Awesome Human')},</strong></p>
                    <p><strong>Ready to hit the road?</strong> 🚗💨 We’ve got an <strong>Auto Loan</strong> just for you! With <strong>low rates</strong> (seriously, we’re talking <strong>amazing</strong> rates), you can drive away with the <strong>car of your dreams</strong>! 🚘 The best part? You can apply in a few clicks. <strong>Don’t make us beg, apply now!</strong></p>
                    <p><strong>Cheers to your new ride! 🎉</strong></p>
                    <p><strong>Your Friendly Bank Team</strong></p>
                """,
                'Credit-Builder Loan': f"""
                    <p><strong>Hey {client_data.get('name', 'Money Master')},</strong></p>
                    <p><strong>We get it, life throws curveballs, and credit scores take a hit.</strong> 😓 But don’t worry, we’ve got your back with our <strong>Credit-Builder Loan</strong>! It's like a <strong>gym membership</strong>, but for your credit score 💪. Apply now and start lifting those points!</p>
                    <p><strong>Let’s rebuild that score together!</strong></p>
                    <p><strong>Your Friendly Bank Team</strong></p>
                """,
                'Home Equity Loan': f"""
                    <p><strong>Dear {client_data.get('name', 'Homeowner Extraordinaire')},</strong></p>
                    <p><strong>Is your home your castle?</strong> 🏰 Well, now it can work for you! With our <strong>Home Equity Loan</strong>, you can unlock the value of your home and make it even <strong>more awesome</strong>. Home renovations, debt consolidation, or vacation fund? You choose! 🌴</p>
                    <p><strong>Apply now — your home deserves it!</strong></p>
                    <p><strong>Your Friendly Bank Team</strong></p>
                """,
                'Mortgage Loan': f"""
                    <p><strong>Hey {client_data.get('name', 'Future Homeowner')},</strong></p>
                    <p><strong>We know you’ve been dreaming of your own home</strong> 🏡. Well, stop dreaming and start <strong>doing</strong>! Our <strong>Mortgage Loan</strong> is here to help you with <strong>competitive rates</strong> and <strong>flexible terms</strong>.</p>
                    <p><strong>Apply today and let’s get you that house!</strong></p>
                    <p><strong>Your Friendly Bank Team</strong></p>
                """,
                'Payday Loan': f"""
                    <p><strong>Hey {client_data.get('name', 'Money Magician')},</strong></p>
                    <p><strong>Life’s a rollercoaster, right?</strong> 🎢 We know things can get tight sometimes, and that’s where our <strong>Payday Loan</strong> comes in! Quick, easy, and designed to get you <strong>back on track</strong>. No need to stress — we’ve got you covered!</p>
                    <p><strong>Apply today and let’s make those stressful days disappear!</strong></p>
                    <p><strong>Your Friendly Bank Team</strong></p>
                """,
                'Student Loan': f"""
                    <p><strong>Hey {client_data.get('name', 'Future CEO')},</strong></p>
                    <p><strong>College life is tough, but we’re here to make it a little easier.</strong> Our <strong>Student Loan</strong> offers <strong>low rates</strong> and <strong>flexible repayment options</strong>. Whether it’s textbooks or late-night pizza (because we’ve all been there 🍕), we’ve got your back!</p>
                    <p><strong>Apply today and take the first step toward your degree (and a future full of success!).</strong></p>
                    <p><strong>Your Friendly Bank Team</strong></p>
                """
            }

            # Sending emails for each loan recommendation
            for loan, recommend in recommendations.items():
                if recommend:
                    message = loan_messages.get(loan, '')
                    send_mail(
                        subject,
                        message,
                        "smartcredit.supp@gmail.com", 
                        [email],  
                        fail_silently=False,
                        html_message=message,
                    )

            return JsonResponse({"status": "success", "message": "Loan recommendations sent with a smile!"})

        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})

    return JsonResponse({"status": "error", "message": "Invalid request method."})