from django.contrib import admin
from account.models import OTTUser, Notification, Result


class HayUserAdmin(admin.ModelAdmin):
    pass


class NotificationAdmin(admin.ModelAdmin):
    pass


class ResultAdmin(admin.ModelAdmin):
    pass

admin.site.register(Result, ResultAdmin)
admin.site.register(OTTUser, HayUserAdmin)
admin.site.register(Notification, NotificationAdmin)