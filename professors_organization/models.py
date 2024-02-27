from django.db import models

from catalogs.models import Grade
from catalogs.models import Subject
from core.models import Professor

# Create your models here.
class Group(models.Model):
    grade_id = models.ForeignKey(Grade, on_delete=models.CASCADE)
    academic_year = models.IntegerField()
    guide_professor_id = models.ForeignKey(Professor, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return "Grade: %s Academic Year: %s Guide: %s" % (self.grade_id,self.academic_year, self.guide_professor_id)


class SubjectProfessor(models.Model):
    professor_id = models.ForeignKey(Professor, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)