from djoser import email
from templated_mail.mail import BaseEmailMessage
from django.contrib.auth.tokens import default_token_generator
from templated_mail.mail import BaseEmailMessage
from djoser.conf import settings
import dotenv
dotenv.load_dotenv()
import os

from djoser import utils
class ActivationEmail(email.ActivationEmail):
    template_name='account/activation.html'
    def get_context_data(self):
        context = super().get_context_data()
        user = context.get("user")

        return context
    
class ConfirmationEmail(BaseEmailMessage):
    template_name = "email/confirmation.html"
    
class PasswordResetEmail(BaseEmailMessage):
    template_name = "account/password_reset.html"

    def get_context_data(self):
        # PasswordResetEmail can be deleted
        context = super().get_context_data()
        front_url= os.getenv('fe_url')
        user = context.get("user")
        context["uid"] = utils.encode_uid(user.pk)
        context["token"] = default_token_generator.make_token(user)
        context["url"] = settings.PASSWORD_RESET_CONFIRM_URL.format(**context)

        context["domain"] = f'{front_url}'
        return context


class PasswordChangedConfirmationEmail(BaseEmailMessage):
    template_name = "email/password_changed_confirmation.html"