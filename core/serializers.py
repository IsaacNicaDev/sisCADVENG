from rest_framework import serializers
from catalogs.serializers import  MaritalStatusSerializer

from .models import *



class LocationSerializer(serializers.ModelSerializer):
    country_id = serializers.CharField(source = 'country_id.name')
    city_id = serializers.CharField(source = 'city_id.name')
    departament_id = serializers.CharField(source = 'departament_id.name')
    zone_id = serializers.CharField(source = 'zone_id.name')
    district_id = serializers.CharField(source = 'district_id.name')
    class Meta:
        model = Location
        fields = ("id", "country_id", "city_id", "departament_id", "zone_id", "district_id", "created_at", "updated_at")
        read_only_fields = ("created_at",)

class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = ("id", "first_name", "second_name", "last_name", "second_lastname", "id_number","phone","consanguinity", "created_at", "updated_at")
        read_only_fields = ("created_at",)


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ("id", "student_code", "picture","first_name","second_name", "last_name", "second_lastname", "location_id","date_birth","nationality_id",
                "address","religion_id","native_language_id","disability_id","birth_certificate","tutor_id","gender_id","created_at", "updated_at")
        read_only_fields = ("created_at",)

class ProfessorSerializer(serializers.ModelSerializer):
    marital_status_id = serializers.PrimaryKeyRelatedField(queryset=MaritalStatus.objects.all())
    
    class Meta:
        model = Professor
        fields = ("id", "first_name","second_name", "last_name", "second_lastname", "age","marital_status_id","phone",
                "number_children","created_at", "updated_at")
        read_only_fields = ("created_at",)

#prueba
class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ("id", "descripcion", "fechainicio", "fechalimite", "notas", "area", "created_at", "updated_at")
        read_only_fields = ("created_at",)
