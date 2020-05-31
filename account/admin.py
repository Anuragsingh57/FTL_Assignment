from django.contrib import admin

# Register your models here.

from .models import User, ActivityPeriods


@admin.register(User)
class UserRegister(admin.ModelAdmin):
    list_display = (
        'id',
        'real_name',
        'time_zone',
        'create_time',
        'user_name'
    )

    search_fields = (
        'real_name',
    )

    list_filter = (
        'is_staff',
    )

    fields = (
        'real_name',
        'time_zone',
        'user_name',
        'is_staff',
    )

@admin.register(ActivityPeriods)
class ActivityPeriodsRegister(admin.ModelAdmin):
    list_display = (
        'user',
        'start_time',
        'end_time',
    )

    fields = (
        'user',
        'start_time',
        'end_time',
    )
