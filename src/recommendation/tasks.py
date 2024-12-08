from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_loan_recommendation_email(subject, message, recipient):
    send_mail(
        subject,
        message,
        "smartcredit.supp@gmail.com",  
        [recipient],
        fail_silently=False,
    )
