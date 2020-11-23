from django.contrib import admin
from .models import (
    UserDataModel
)

@admin.register(UserDataModel)
class RecordsAdmin(admin.ModelAdmin):
    list_display = ['username', 'created_on', 'record_file']
    # admin.site.register(UserDataModel
