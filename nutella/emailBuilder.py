from __future__ import print_function
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException

configuration = sib_api_v3_sdk.Configuration()
configuration.api_key[
    "api-key"
] = "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"

api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
    sib_api_v3_sdk.ApiClient(configuration)
)
subject = "from the Python SDK!"
sender = {"name": "Sendinblue", "email": "contact@sendinblue.com"}
replyTo = {"name": "Sendinblue", "email": "contact@sendinblue.com"}
html_content = (
    "<html><body><h1>This is my first transactional email </h1></body></html>"
)
to = [{"email": "example@example.com", "name": "Jane Doe"}]
params = {"parameter": "My param value", "subject": "New Subject"}
send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
    to=to,
    html_content=html_content,
    sender=sender,
    subject=subject,
)

try:
    api_response = api_instance.send_transac_email(send_smtp_email)
    print(api_response)
except ApiException as e:
    print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
