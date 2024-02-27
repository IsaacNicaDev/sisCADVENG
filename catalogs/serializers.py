from rest_framework import serializers

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


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = ("id", "name", "created_at", "updated_at")
        read_only_fields = ("created_at",)


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ("id", "name", "created_at", "updated_at")
        read_only_fields = ("created_at",)


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ("id", "name", "created_at", "updated_at")
        read_only_fields = ("created_at",)


class MunicipalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipality
        fields = ("id", "name", "created_at", "updated_at")
        read_only_fields = ("created_at",)


class EducationalLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalLevel
        fields = ("id", "name", "created_at", "updated_at")
        read_only_fields = ("created_at",)


class ModalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Modality
        fields = ("id", "name", "created_at", "updated_at")
        read_only_fields = ("created_at",)


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ("id", "name", "created_at", "updated_at")
        read_only_fields = ("created_at",)


class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = ("id", "name", "created_at", "updated_at")
        read_only_fields = ("created_at",)


class EducationalInstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalInstitution
        fields = ("id", "name", "created_at", "updated_at")
        read_only_fields = ("created_at",)


class EnrolmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnrolmentType
        fields = ("id", "name", "created_at", "updated_at")
        read_only_fields = ("created_at",)


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ("id", "name", "created_at", "updated_at")
        read_only_fields = ("created_at",)


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("id", "name", "created_at", "updated_at")
        read_only_fields = ("created_at",)


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ("id", "name", "created_at", "updated_at")
        read_only_fields = ("created_at",)


class EthnicitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ethnicity
        fields = ("id", "name", "created_at", "updated_at")
        read_only_fields = ("created_at",)


class DisabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Disability
        fields = ("id", "name", "created_at", "updated_at")
        read_only_fields = ("created_at",)


class ReligionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Religion
        fields = ("id", "name", "created_at", "updated_at")
        read_only_fields = ("created_at",)


class DepartamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departament
        fields = ("id", "name", "created_at", "updated_at")
        read_only_fields = ("created_at",)


class DepartamentalDelegationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartamentalDelegation
        fields = ("id", "name", "created_at", "updated_at")
        read_only_fields = ("created_at",)


class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = ("id", "name", "created_at", "updated_at")
        read_only_fields = ("created_at",)


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ("id", "name", "created_at", "updated_at")
        read_only_fields = ("created_at",)

class MaritalStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaritalStatus
        fields = ("id", "name", "created_at", "updated_at")
        read_only_fields = ("created_at",)        
