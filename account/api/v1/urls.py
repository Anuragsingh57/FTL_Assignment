from django.urls import path, include
from rest_framework import (
    routers
)
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    UserAPIViewSet,
    ActivityPeriodsAPIViewSet
)

router = routers.SimpleRouter(trailing_slash=False)
router.register('users', UserAPIViewSet)
router.register('activityperiods', ActivityPeriodsAPIViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# Add Multiple Format Support
urlpatterns = format_suffix_patterns(urlpatterns)