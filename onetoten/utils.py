from twilio.rest import TwilioRestClient

account = "AC62a425b1f396f890f96bed5b598ee62f"
token = "5245080b76da4d1e818a770ba4479a67"
client = TwilioRestClient(account, token)
from_number = "19802014736"


def send_text(to_number, message_content):
    result = client.messages.create(to=to_number, from_=from_number, body=message_content)
    return result
