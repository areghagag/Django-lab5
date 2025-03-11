from django.db import models

from course.models import Course


# Create your models here.
class Trainee(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    @classmethod
    def getalltrainees(cls):
        return cls.objects.all()

    @classmethod
    def gettraineebyid(cls, id):
        return cls.objects.get(id=id)