''' admin '''
from django.contrib import admin

from .models import VDay
# Register your models here.


@admin.register(VDay)
class VDayAdmin(admin.ModelAdmin):
    ''' vday on admin '''
    pass
