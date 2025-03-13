from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView

from .models import Trainee
from .forms import TraineeForm
from course.models import Course




# Create your views here.
class TraineeListView(ListView):
    model = Trainee
    template_name = 'list.html'
    context_object_name = 'trainees'
def trainee_list(request):
    context={'trainees':Trainee.getalltrainees()}
    return render(request,'list.html',context)

class  TraineeAddView(View):
    def get(self,request):
        form=TraineeForm()
        return render(request,'add.html',{'form':form})

    def post(self,request):
        form = TraineeForm(request.POST)
        if form.is_valid():
            Trainee.objects.create(
                name=request.POST.get('name'),
                email=request.POST.get('email'),
                course_id_id=request.POST.get('course')
            )
            return redirect('trainee_list')
        return render(request, 'add.html', {'form': form})

# def add_trainee(request):
#     form = TraineeForm()
#
#     if request.method == 'POST':
#         form = TraineeForm(request.POST)
#         if form.is_valid():
#             objectofcourse = Course.objects.get(id=form.cleaned_data['course'])
#             Trainee.objects.create(
#                 name=form.cleaned_data['name'],
#                 email=form.cleaned_data['email'],
#                 course_id=objectofcourse
#             )
#             return redirect('trainee_list')
#
#     return render(request, 'add.html', {'form': form})


class TraineeUpdateView(View):
    def get(self, request, pk):
        trainee = Trainee.objects.filter(id=pk).first()
        if not trainee:
            return redirect('trainee_list')

        form = TraineeForm(initial={'name': trainee.name, 'email': trainee.email, 'course': trainee.course_id_id})
        courses = Course.objects.all()  # ✅ تأكد من تمرير جميع الكورسات للقالب
        return render(request, 'update.html', {'form': form, 'trainee': trainee, 'courses': courses})

    def post(self, request, pk):
        trainee = Trainee.objects.filter(id=pk).first()
        if not trainee:
            return redirect('trainee_list')

        form = TraineeForm(request.POST)
        if form.is_valid():
            trainee.name = request.POST.get('name', trainee.name)
            trainee.email = request.POST.get('email', trainee.email)
            trainee.course_id_id = request.POST.get('course', trainee.course_id_id)
            trainee.save()
            return redirect('trainee_list')

        courses = Course.objects.all()
        return render(request, 'update.html', {'form': form, 'trainee': trainee, 'courses': courses})
# def update_trainee(request,id):
#     trainee = Trainee.objects.get(id=id)
#     courses = Course.objects.all()
#     if request.method == "POST":
#         trainee.name = request.POST.get('name', trainee.name)
#         trainee.email = request.POST.get('email', trainee.email)
#         trainee.course_id = Course.objects.get(id=request.POST.get('course'))
#         trainee.save()
#         return redirect('trainee_list')
#     return render(request, 'update.html', {'trainee': trainee, 'courses': courses})

class TraineeDetailView(DetailView):
    model = Trainee
    template_name = 'show_details.html'
    context_object_name = 'trainee'


class  TraineeDeleteView(DeleteView):
    model = Trainee
    template_name = 'delete.html'
    success_url = reverse_lazy('trainee_list')

def delete_trainee(request, id):
    trainee = Trainee.objects.get(id=id)
    trainee.delete()
    return redirect('trainee_list')
