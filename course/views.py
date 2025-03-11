from django.shortcuts import render, redirect

from .models import Course


# Create your views here.
def course_list(request):
    courses = Course.getallcourse()
    context = {'courses': courses}
    return render(request, 'course/list.html', context)
def add_course(request):
    if request.method == 'POST':
        title=request.POST['title']
        description=request.POST['description']
        Course.objects.create(title=title,description=description)
        return redirect('course_list')
    return render(request, 'course/add.html')
def update_course(request,id):
    course=Course.objects.get(id=id)
    if request.method == 'POST':
        course.title = request.POST.get('title', course.title)
        course.description = request.POST.get('description', course.description)
        course.save()
        return redirect('course_list')
    return render(request, 'course/update.html', {'course': course})


def delete_course(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('course_list')
