from rest_framework import routers

from .api import *

router = routers.DefaultRouter()

router.register('locations', LocationViewSet, 'Locations'),
router.register('tutors', TutorViewSet, 'Tutors')
router.register('students', StudentViewSet, 'Students')
router.register('professors', ProfessorViewSet, 'Professors')

urlpatterns = router.urls