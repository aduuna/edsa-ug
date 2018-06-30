from django.contrib import admin

from .models import WelcomeMessage,AlertMessage
# Register your models here.

admin.site.register(WelcomeMessage)
admin.site.register(AlertMessage)
