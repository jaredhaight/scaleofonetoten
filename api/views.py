from django.http import HttpResponse
from django_twilio.decorators import twilio_view
from twilio.twiml import Response
from account.models import OTTUser, Result
from onetoten.utils import log_message

@twilio_view
def sms(request):
    resp = Response()
    from_number = request.POST["From"]
    body = request.POST["Body"]
    log_message("Got from number: " + from_number[:10])
    try:
        user = OTTUser.objects.filter(phone_number=from_number[:10]).first()
    except:
        user = None

    try:
        body = int(body)
    except:
        body = "Sorry, I only understand numbers."

    if type(body) == int and user:
        result = Result(value=body, user=user, source=from_number)
        result.save()
        resp.message("Got response of %s for %s" % (body, user))
    elif user:
        resp.message(body)
    else:
        resp.message("Please sign up for an account at http://www.scaleofonetoten.com")
    return HttpResponse(resp.toxml(), content_type="text/xml")