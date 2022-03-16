from django.core.mail import EmailMessage
from sitesettings.models import SMTPSetting
from django.core.mail.backends.smtp import EmailBackend
from decouple import config


class Util:

    @staticmethod
    def send_mail_register(data):
        smtpsetting = SMTPSetting.objects.last()
        backend = EmailBackend(port=587,
                               host='smtp.gmail.com',
                               username=config('EMAIL_HOST_USERNAME'),
                               password=config('EMAIL_HOST_PASSWORD'),
                               fail_silently=False
                               )

        email = EmailMessage(subject= data['email_subject'], body=data['email_body'], from_email= config('EMAIL_HOST_USERNAME'),to=[data['email_receiver']], connection=backend)
        email.send()