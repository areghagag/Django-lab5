from django.db import models

# Create your models here.
class Course(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    description=models.TextField()
    @classmethod
    def getallcourse(cls):
         return cls.objects.all()

    @classmethod
    def getcoursebyid(cls, id):
         return cls.objects.get(id=id)