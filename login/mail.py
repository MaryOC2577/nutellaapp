import os
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException


def send_reset_password_mail(email, token, user):
    # print(email, token)
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key["api-key"] = os.getenv("SEND_IN_BLUE_API")

    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
        sib_api_v3_sdk.ApiClient(configuration)
    )
    subject = "Renouvellement mot de passe Nutella"
    sender = {"name": "Sendinblue", "email": "contact@sendinblue.com"}
    html_content = (
        f"""<html><body><h1><a href='127.0.0.1:8000/login/password_reset/{token}'>"""
        """Renouveller votre mot de passe.</a></h1><br></body></html>"""
    )
    to = [{"email": email, "name": user}]
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        to=to,
        html_content=html_content,
        sender=sender,
        subject=subject,
    )
    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        return api_response
    except ApiException as e:
        print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
        return None
