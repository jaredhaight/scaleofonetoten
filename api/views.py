from django.http import HttpResponse

from django_twilio.decorators import twilio_view
from twilio.twiml import Response

from dashboard.models import Result
from profile.models import HayUser

@twilio_view
def sms(request):
    resp = Response()
    from_number = request.POST["From"]
    body = request.POST["Body"]
    try:
        user = HayUser.objects.filter(from_number[1:]).first()
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