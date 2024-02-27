from rest_framework import viewsets, permissions

from .models import Enrollment
from .serializers import EnrollmentSerializer


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EnrollmentSerializer


