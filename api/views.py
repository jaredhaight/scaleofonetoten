
from django.http import HttpResponse

from django_twilio.decorators import twilio_view
from twilio.twiml import Response
from dashboard.models import Result

@twilio_view
def sms(request):
    resp = Response()
    resp.message("SCALE OF ONE TO A BILLION!")
    return HttpResponse(resp.toxml(), content_type="text/xml")