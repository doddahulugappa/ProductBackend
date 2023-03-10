from celery import shared_task
from django.conf import settings
from django.contrib.auth.models import User
from datetime import date
from .models import ActiveUser
from django.core.mail import EmailMessage


@shared_task(bind=True)
def send_activation_mail(self):
    today = date.today()
    user_obj = User.objects.filter(date_joined__lte=today)
    for user in user_obj:
        try:
            active_user = ActiveUser.objects.get(pk=user)
            if active_user.activated:
                print(f"User {user} is already activated")
            else:
                send_email(user)
                active_user.activated = True
                active_user.save()
                print("User Activated")
        except ActiveUser.DoesNotExist:
            send_email(user)
            active_user = ActiveUser(activated=True, user=user)
            active_user.save()
            print("User Activated")

    return f'Success:Mail has been sent'


def send_email(user):
    message = """
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html; charset=ISO-8859-1">
    </head>
    <body bgcolor="#ffffff" text="#000000">
    Dear """+user.username+""", <br><br>
    Your account has been activated! <br>
    Kindly visit our <a href="https://www.skyloov.com/"> website </a> to explore services provided by us!<br><br>
    <div class="moz-signature"><i><br>
    <br>
    Regards<br>
    SkyLoov Digital Solutions,<br>
    </i></div>
    </body>
    </html>
    """

    subject = 'Welcome to skyloov digital solutions'
    mail = EmailMessage(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [user.email],
    )
    mail.fail_silently = False
    mail.content_subtype = 'html'
    mail.send()

