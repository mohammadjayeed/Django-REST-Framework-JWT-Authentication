from django.core.mail import send_mail
from django.conf import settings
import random
from .models import User
def send_otp(email):
    subject = "Account Verification Email From JWT App"
    otp = random.randint(1000, 9999)
    message = f"Your OTP is {otp}"
    email_from = settings.EMAIL_HOST
    send_mail(subject,message, email_from,[email])
    user_obj = User.objects.get(email=email)
    user_obj.otp = otp
    user_obj.save()