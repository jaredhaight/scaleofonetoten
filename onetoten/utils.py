from twilio.rest import TwilioRestClient
from onetoten.local_settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN
client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
from_number = "19802014736"


def send_text(to_number, message_content):
    result = client.messages.create(to=to_number, from_=from_number, body=message_content)
    return result