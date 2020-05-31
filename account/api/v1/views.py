from rest_framework import permissions

from .serializers import UserSerializer, ActivityPeriodsSerializer
from account.models import ActivityPeriods
from django.contrib.auth import get_user_model
from rest_framework.viewsets import (
    ModelViewSet
)
User = get_user_model()

class UserAPIViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ActivityPeriodsAPIViewSet(ModelViewSet):
    """
    API endpoint that allows ActivityPeriods to be viewed or edited.
    """
    queryset = ActivityPeriods.objects.all()
    serializer_class = ActivityPeriodsSerializer
