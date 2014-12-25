from django.core.management.base import BaseCommand, CommandError
from profile.models import Notification
import datetime
from onetoten.utils import send_text


def log_message(message):
    with open("/tmp/sendmessages_log", "a") as logfile:
        logfile.write(datetime.datetime.now().isoformat()+" - " + message + "\n")


class Command(BaseCommand):
    def handle(self, *args, **options):
        notifications = Notification.objects.filter(time_to_send__hour=datetime.datetime.now().hour)
        log_message("Notifications: " + str(notifications))

        for notification in notifications:
            if notification.type == "TEXT" and notification.user.phone_number:
                log_message("Sending text to: " + notification.user.phone_number)
                send_text(notification.user.phone_number, "How are you doing today?")