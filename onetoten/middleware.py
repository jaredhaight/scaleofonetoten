import pytz
from django.utils import timezone


class TimezoneMiddleware(object):
    def process_request(self, request):
        tzname = None
        try:
            tzname = request.user.timezone
        except:
            pass
        if tzname:
            timezone.activate(pytz.timezone(tzname))
        else:
            timezone.deactivate()