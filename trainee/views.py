from django.shortcuts import render, redirect

from .forms import TraineeForm
from .models import Trainee
from course.models import Course



# Create your views here.
def trainee_list(request):
    context={'trainees':Trainee.getalltrainees()}
    return render(request,'list.html',context)
def add_trainee(request):
    form = TraineeForm()

    if request.method == 'POST':
        form = TraineeForm(request.POST)
        if form.is_valid():
            objectofcourse = Course.objects.get(id=form.cleaned_data['course'])
            Trainee.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                course_id=objectofcourse
            )
            return redirect('trainee_list')

    return render(request, 'add.html', {'form': form})

def update_trainee(request,id):
    trainee = Trainee.objects.get(id=id)
    courses = Course.objects.all()
    if request.method == "POST":
        trainee.name = request.POST.get('name', trainee.name)
        trainee.email = request.POST.get('email', trainee.email)
        trainee.course_id = Course.objects.get(id=request.POST.get('course'))
        trainee.save()
        return redirect('trainee_list')
    return render(request, 'update.html', {'trainee': trainee, 'courses': courses})
def delete_trainee(request, id):
    trainee = Trainee.objects.get(id=id)
    trainee.delete()
    return redirect('trainee_list')
