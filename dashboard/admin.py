from django.contrib import admin
from dashboard.models import Result


class ResultAdmin(admin.ModelAdmin):
    pass

admin.site.register(Result, ResultAdmin)