from rest_framework import routers

from .api import EnrollmentViewSet

router = routers.DefaultRouter()

router.register('enrollments', EnrollmentViewSet, 'enrollments'),


urlpatterns = router.urls