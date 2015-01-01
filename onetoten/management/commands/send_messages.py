from django.core.management.base import BaseCommand, CommandError
from account.models import Notification
import datetime
from onetoten.utils import send_text, log_message


class Command(BaseCommand):
    def handle(self, *args, **options):
        notifications = Notification.objects.filter(time_to_send__hour=datetime.datetime.now().hour)
        log_message("Notifications: " + str(notifications))

        for notification in notifications:
            if notification.type == "TEXT" and notification.user.phone_number:
                log_message("Sending text to: " + notification.user.phone_number)
                send_text(notification.user.phone_number, "How are you doing today?")