import random

from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
from django.conf import settings

from accounts.models import User


def send_otp_via_email(email):
    subject = 'Your account verification email'
    otp = random.randint(1000, 9999)
    context = {'otp': otp}
    message = render_to_string('otp_email_template.html', context)
    from_email = settings.EMAIL_HOST_USER
    to_email = [email]
    try:
        send_mail(subject, '', from_email, to_email, html_message=message)
        user_obj = User.objects.get(email=email)
        user_obj.otp = otp
        user_obj.save()
        print("Отправлено")
    except BadHeaderError:
        print('Invalid header found.')



# старое обычное отправление otp коды без верстки
# def send_otp_via_email(email):
#     subject = f'Your account verification email'
#     otp = random.randint(1000, 9999)
#     message = f'Your otp is {otp}'
#     from_email = settings.EMAIL_HOST
#     send_mail(subject, message, from_email, [email])
#     user_obj = User.objects.get(email=email)
#     user_obj.otp = otp
#     user_obj.save()
#     print("отправлено")