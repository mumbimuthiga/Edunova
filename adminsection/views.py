from django.shortcuts import render
from .models import Program

# Create your views here.

def dashboard(request):
    return render(request, 'admin/dashboard.html')

def profile(request):
    return render(request,'admin/profile.html')

def programs(request):
    programs=Program.objects.all()
    return render(request,'admin/programs.html',{'programs':programs})

def jobs(request):
    return render(request,'admin/jobs.html')

def skills(request):
    return render(request,'admin/skills.html')

def edit_profile(request):
    return render(request,'admin/edit_profile.html')