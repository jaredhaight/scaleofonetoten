from django.contrib import admin
from profile.models import HayUser, Notification


class HayUserAdmin(admin.ModelAdmin):
    pass


class NotifcationAdmin(admin.ModelAdmin):
    pass


admin.site.register(HayUser, HayUserAdmin)
admin.site.register(Notification, NotifcationAdmin)