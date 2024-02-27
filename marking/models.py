from django.db import models

# Create your models here.
class Marking(models.Model):
    subject_id = models.ForeignKey(Subject)
    professor_id = models.ForeignKey(Professor)
    student_id = models.ForeignKey(Student)
    marking = models.IntegerField()
    evaluation_cutoff = models.ForeignKey()
    grade_id = models.ForeignKey(Grade)
    group_id = models.ForeignKey(Group)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)