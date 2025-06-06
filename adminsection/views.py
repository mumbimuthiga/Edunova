import requests
from django.shortcuts import render
from programs.models import Programs



# Create your views here.

def dashboard(request):
    return render(request, 'admin/dashboard.html')

def profile(request):
    return render(request,'admin/profile.html')

def programs_view(request):
    programs=Programs.objects.all()
    # print (programs)
    # for program in programs:
    #     print(program) 
    return render(request,'admin/programs.html',{'programs':programs})

def jobs(request):
    url = "https://api.adzuna.com/v1/api/jobs/gb/search/1"
    params = {
        "app_id": "21777ecc", 
        "app_key": "32485eabf03019b39cb8b202fb77367e",  
        "what": "developer",   
        "where": "london"      
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        # print(data)  
        jobs = data.get("results", [])
    except requests.RequestException as e:
        print("API error:", e)
        jobs = []

    return render(request, 'admin/jobs.html', {"jobs": jobs})

def skills(request):
    return render(request,'admin/skills.html')

def edit_profile(request):
    return render(request,'admin/edit_profile.html')