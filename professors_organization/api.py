from rest_framework import viewsets, permissions

from .models import Group
from .models import SubjectProfessor
from .serializers import GroupSerializer
from .serializers import SubjectProfessorSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = GroupSerializer

class SubjectProfessorViewSet(viewsets.ModelViewSet):
    queryset = SubjectProfessor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SubjectProfessorSerializer
