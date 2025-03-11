from django import forms
from course.models import Course
from .models import Trainee


class TraineeForm(forms.Form):
    name=forms.CharField(max_length=100,label='Full Name',required=True)
    email=forms.EmailField(required=True,label='Email')
    course=forms.ChoiceField(choices=[(course.id,course.title)
                                     for course in Course.getallcourse()])