from django.http import HttpResponse

from django_twilio.decorators import twilio_view
from twilio.twiml import Response

from dashboard.models import Result

@twilio_view
def sms(request):
    resp = Response()
    from_number = None
    body = None
    if request.POST.get("from"):
        from_number = request.POST["from"]
    if request.POST.get("body"):
        body = request.POST["body"]
    if from_number and body:
        resp.message("You said %s from %s" % (from_number, body))
    elif from_number:
        resp.message("You send a message from %s" % from_number)
    elif body:
        resp.message("You said %s" % body)
    else:
        resp.message("I have no idea what's going on.")
    return HttpResponse(resp.toxml(), content_type="text/xml")