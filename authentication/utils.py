from django.core.mail import EmailMessage
from sitesettings.models import SMTPSetting
from django.core.mail.backends.smtp import EmailBackend



class Util:

    @staticmethod
    def send_mail_register(data):
        smtpsetting = SMTPSetting.objects.last()
        backend = EmailBackend(port=smtpsetting.email_port,
                               host=smtpsetting.email_host,
                               username=smtpsetting.email_host_user,
                               password=smtpsetting.email_host_password,
                               fail_silently=False
                               )

        email = EmailMessage(subject= data['email_subject'], body=data['email_body'], from_email= smtpsetting.email_host_user,to=[data['email_receiver']], connection=backend)
        email.send()