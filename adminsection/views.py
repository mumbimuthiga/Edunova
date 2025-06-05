from django.shortcuts import render

from programs.models import Programs



# Create your views here.

def dashboard(request):
    return render(request, 'admin/dashboard.html')

def profile(request):
    return render(request,'admin/profile.html')

def programs_view(request):
    programs=Programs.objects.all()
    print (programs)
    for program in programs:
        print(program) 
    return render(request,'admin/programs.html',{'programs':programs})

def jobs(request):
    return render(request,'admin/jobs.html')

def skills(request):
    return render(request,'admin/skills.html')

def edit_profile(request):
    return render(request,'admin/edit_profile.html')