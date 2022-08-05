from django.contrib import admin
from .models import Profile, DiaseseInfo, VaccinateInfo


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'full_name', 'bday', 'passport_num', 'oms', 'snils')
    search_fields = ('user__username',)


@admin.register(VaccinateInfo)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'vaccine_date', 'record_number', 'series')
    search_fields = ('user__username',)

@admin.register(DiaseseInfo)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'recovery_date', 'record_number')
    search_fields = ('user__username',)