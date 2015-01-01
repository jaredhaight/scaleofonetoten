from django.forms import fields
from django.forms import ModelForm, ChoiceField
from django.forms.util import from_current_timezone
from django.forms.util import to_current_timezone
from django.utils import timezone
import pytz
import datetime
from account.models import OTTUser, Notification, NOTIFICATION_CHOICES


class TzAwareTimeField(fields.TimeField):
    def prepare_value(self, value):
        if isinstance(value, datetime.datetime):
            value = to_current_timezone(value).time()
        return super(TzAwareTimeField, self).prepare_value(value)

    def clean(self, value):
        value = super(TzAwareTimeField, self).to_python(value)
        print value
        dt = to_current_timezone(timezone.now())
        print dt
        new_time = dt.replace(
            hour=value.hour, minute=value.minute,
            second=value.second, microsecond=value.microsecond)
        print from_current_timezone(new_time)
        return from_current_timezone(new_time)


class OTTUserForm(ModelForm):
    class Meta:
        model = OTTUser
        fields = ['email', 'phone_number', 'timezone']


class NotificationForm(ModelForm):
    type = ChoiceField(choices=NOTIFICATION_CHOICES, label="Type of Notification")
    time_to_send = TzAwareTimeField()
    class Meta:
        model = Notification
        fields = ['type', 'time_to_send']