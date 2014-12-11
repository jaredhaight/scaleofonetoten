from django.core.management.base import BaseCommand, CommandError
from profile.models import Notification
import datetime
from onetoten.utils import send_text


class Command(BaseCommand):
    def handle(self, *args, **options):
        start_time = (datetime.datetime.now()+datetime.timedelta(minutes=-15)).time()
        end_time = (datetime.datetime.now()+datetime.timedelta(minutes=15)).time()
        notifications = Notification.objects.filter(time_to_send__range=(start_time, end_time))

        for notification in notifications:
            if notification.type == "TEXT" and notification.user.phone_number:
                send_text(notification.user.phone_number, "How are you doing today?")