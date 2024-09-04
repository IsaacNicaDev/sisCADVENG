from rest_framework import viewsets, permissions

from .models import *
from .serializers import *


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LocationSerializer

class TutorViewSet(viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TutorSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = StudentSerializer

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProfessorSerializer


#prueba
class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = GoalSerializer
