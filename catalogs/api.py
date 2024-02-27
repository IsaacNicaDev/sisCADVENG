from rest_framework import viewsets, permissions

from .models import Gender
from .models import Grade
from .models import Subject
from .models import Municipality
from .models import EducationalLevel
from .models import Modality
from .models import Section
from .models import Shift
from .models import EducationalInstitution
from .models import EnrolmentType
from .models import City
from .models import Country
from .models import Language
from .models import Ethnicity
from .models import Disability
from .models import Religion
from .models import Departament
from .models import DepartamentalDelegation
from .models import Zone
from .models import District
from .models import MaritalStatus
from .serializers import GenderSerializer
from .serializers import GradeSerializer
from .serializers import SubjectSerializer
from .serializers import MunicipalitySerializer
from .serializers import EducationalLevelSerializer
from .serializers import ModalitySerializer
from .serializers import SectionSerializer
from .serializers import ShiftSerializer
from .serializers import EducationalInstitutionSerializer
from .serializers import EnrolmentTypeSerializer
from .serializers import CitySerializer
from .serializers import CountrySerializer
from .serializers import LanguageSerializer
from .serializers import EthnicitySerializer
from .serializers import DisabilitySerializer
from .serializers import ReligionSerializer
from .serializers import DepartamentSerializer
from .serializers import DepartamentalDelegationSerializer
from .serializers import ZoneSerializer
from .serializers import DistrictSerializer
from .serializers import MaritalStatusSerializer

class GenderViewSet(viewsets.ModelViewSet):
    queryset = Gender.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = GenderSerializer

class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = GradeSerializer 

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SubjectSerializer

class MunicipalityViewSet(viewsets.ModelViewSet):
    queryset = Municipality.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MunicipalitySerializer

class EducationalLevelViewSet(viewsets.ModelViewSet):
    queryset = EducationalLevel.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EducationalLevelSerializer

class ModalityViewSet(viewsets.ModelViewSet):
    queryset = Modality.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ModalitySerializer

class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SectionSerializer 

class ShiftViewSet(viewsets.ModelViewSet):
    queryset = Shift.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ShiftSerializer

class EducationalInstitutionViewSet(viewsets.ModelViewSet):
    queryset = EducationalInstitution.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EducationalInstitutionSerializer

class EnrolmentTypeViewSet(viewsets.ModelViewSet):
    queryset = EnrolmentType.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EnrolmentTypeSerializer 

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CitySerializer 

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CountrySerializer

class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LanguageSerializer 

class EthnicityViewSet(viewsets.ModelViewSet):
    queryset = Ethnicity.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EthnicitySerializer 

class DisabilityViewSet(viewsets.ModelViewSet):
    queryset = Disability.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DisabilitySerializer 

class ReligionViewSet(viewsets.ModelViewSet):
    queryset = Religion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ReligionSerializer 

class DepartamentViewSet(viewsets.ModelViewSet):
    queryset = Departament.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DepartamentSerializer 

class DepartamentalDelegationViewSet(viewsets.ModelViewSet):
    queryset = DepartamentalDelegation.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DepartamentalDelegationSerializer 

class ZoneViewSet(viewsets.ModelViewSet):
    queryset = Zone.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ZoneSerializer

class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DistrictSerializer

class MaritalStatusViewSet(viewsets.ModelViewSet):
    queryset = MaritalStatus.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MaritalStatusSerializer    
