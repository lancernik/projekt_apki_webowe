from django.contrib import admin

from surveys.models import Drug

# Register your models here.



@admin.register(Drug)
class DrugtAdmin(admin.ModelAdmin):
    pass