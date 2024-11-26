from django.db import models
from catalogs.models import *


# Create your models here.

class Location(models.Model):
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)
    departament_id = models.ForeignKey(Departament, on_delete=models.CASCADE)
    zone_id = models.ForeignKey(Zone, on_delete=models.CASCADE)
    district_id = models.ForeignKey(District, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return "%s %s %s %s %s" % (self.country_id, self.city_id, self.departament_id, self.zone_id, self.district_id)

class Tutor(models.Model):
    first_name = models.CharField(max_length=15)
    second_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    second_lastname = models.CharField(max_length=15)
    id_number = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=15, unique=True)
    consanguinity = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return "%s %s %s %s" % (self.first_name, self.second_name, self.last_name, self.second_lastname)

class Student(models.Model):
    student_code = models.CharField(max_length=30, unique=True)
    picture = models.ImageField(null=True, upload_to='foto')
    first_name = models.CharField(max_length=15)
    second_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    second_lastname = models.CharField(max_length=15)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)
    date_birth = models.DateField()
    nationality_id = models.ForeignKey(Country, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    religion_id = models.ForeignKey(Religion, on_delete=models.CASCADE)
    native_language_id = models.ForeignKey(Language, on_delete=models.CASCADE)
    disability_id = models.ForeignKey(Disability, on_delete=models.CASCADE)
    birth_certificate = models.BooleanField(unique=True)
    tutor_id = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    gender_id = models.ForeignKey(Gender, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return "%s %s %s %s" % (self.first_name, self.second_name, self.last_name, self.second_lastname)

class Professor(models.Model):
    first_name = models.CharField(max_length=15)
    second_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    second_lastname = models.CharField(max_length=15)
    age = models.IntegerField()
    marital_status_id = models.ForeignKey(MaritalStatus, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, unique=True)
    number_children = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return "%s %s %s %s" % (self.first_name, self.second_name, self.last_name, self.second_lastname,
        self.age, self.marital_status_id, self.phone, self.number_children)
    

#prueba
class Goal(models.Model):
    descripcion = models.CharField(max_length=100)
    fechainicio = models.DateField(null=True, blank=True)
    fechalimite = models.DateField(null=True, blank=True)
    notas = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return "%s %s %s %s %s" % (self.descripcion, self.fechainicio, self.fechalimite, self.notas, self.area)
