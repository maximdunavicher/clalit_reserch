from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import ARule, Disease

admin.site.register(ARule)
admin.site.register(Disease)