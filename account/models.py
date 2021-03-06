from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin



NOTIFICATION_CHOICES = (
    ("EMAIL", "Email"),
    ("TEXT", "Text")
)

DAY_CHOICES = (
    ('SUNDAY', "Sunday"),
    ('MONDAY', "Monday"),
    ("TUESDAY", "Tuesday"),
    ("WEDNESDAY", "Wednesday"),
    ("THURSDAY", "Thursday"),
    ("FRIDAY", "Friday"),
    ("SATURDAY", "Saturday")
)

TIMEZONE_CHOICES = (
    ('US/Alaska', "Alaska"),
    ('US/Arizona', "Arizona"),
    ('US/Central', "Central"),
    ('US/Eastern', "Eastern"),
    ('US/Hawaii', "Hawaii"),
    ("US/Indiana-Starke", "Indiana-Starke"),
    ('US/Mountain', "Mountain"),
    ('US/Pacific', "Pacific")
)


class OTTUserManager(BaseUserManager):
    def create_user(self, email_id, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email_id:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=OTTUserManager.normalize_email(email_id)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        u = self.create_user(email, password=password)
        u.is_admin = True
        u.is_superuser = True
        u.save(using=self._db)
        return u


class OTTUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        db_index=True,
    )
    phone_number = models.CharField(null=True, max_length=12)
    phone_verified = models.BooleanField(editable=False, default=False)
    email_verified = models.BooleanField(editable=False, default=False)
    timezone = models.CharField(default="US/Eastern", choices=TIMEZONE_CHOICES, max_length=24)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = OTTUserManager()

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __unicode__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin


class Notification(models.Model):
    type = models.CharField(max_length=10, choices=NOTIFICATION_CHOICES, default="text")
    #day_to_send = models.CharField(max_length=7, choices=DAY_CHOICES)
    time_to_send = models.DateTimeField(null=True)
    user = models.ForeignKey(OTTUser)

    def create_notification(self, type, days, time):
        self.type = type
        self.time_to_send = time
        self.save()

    def __unicode__(self):
        return "%s - %s" % (self.id, self.user.email)


class Result(models.Model):
    # source of the feedback (phone number, email address, etc)
    source = models.CharField(editable=False, max_length=255)
    value = models.IntegerField()
    note = models.TextField(blank=True, null=True)
    user = models.ForeignKey(OTTUser)
    time = models.DateTimeField()

    def save(self, *args, **kwargs):
        self.time = datetime.now()
        super(Result, self).save(*args, **kwargs)