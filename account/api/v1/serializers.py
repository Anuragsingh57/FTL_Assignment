from pyexpat import model

from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from account.models import ActivityPeriods

from rest_framework import (
    serializers,
    status,
)
from rest_framework.response import Response

USER = get_user_model()


class ActivityPeriodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriods
        fields = (
            'user',
            'start_time',
            'end_time',

        )
        write_only_fields = (
            'user',
        )


class UserSerializer(serializers.ModelSerializer):
    activity_periods = ActivityPeriodsSerializer(many=True, read_only=True)
    class Meta:
        model = USER
        fields = (
            'id',
            'real_name',
            'time_zone',
            'user_name',
            'activity_periods',
        )
        read_only_fields = (
            'create_time',
            'activity_periods',
        )
        write_only_fields = (
            'id',
            'user_name',
        )

