from django.db import models
from datetime import datetime
from profile.models import HayUser


class Result(models.Model):
    # source of the feedback (phone number, email address, etc)
    source = models.CharField(editable=False, max_length=255)
    value = models.IntegerField()
    note = models.TextField(blank=True, null=True)
    user = models.ForeignKey(HayUser)
    time = models.DateTimeField()

    def save(self, *args, **kwargs):
        self.time = datetime.now()
        super(Result, self).save(*args, **kwargs)