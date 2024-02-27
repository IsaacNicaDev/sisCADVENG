from rest_framework import routers

from .api import GroupViewSet
from .api import SubjectProfessorViewSet

router = routers.DefaultRouter()

router.register('groups', GroupViewSet, 'groups'),
router.register('subject-professor', SubjectProfessorViewSet, 'subject-professor'),


urlpatterns = router.urls