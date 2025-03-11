from django.shortcuts import render,redirect
from django.contrib import messages

# Create your views here.
def register_user(request):
    return render(request,'register.html')

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    request.session.flush()  # Clear session
    messages.success(request, "Logged out successfully.")
    return redirect('login')
