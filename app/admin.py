from django.contrib import admin
from django.apps import AppConfig

from .models import *

admin.site.register(User)

class AppConfig(AppConfig):
    name = 'app'

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass
