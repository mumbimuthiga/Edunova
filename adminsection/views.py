import requests
from django.shortcuts import render
from programs.models import Programs
from django.http import JsonResponse
import xml.etree.ElementTree as ET



# Create your views here.

def dashboard(request):
    num_courses=Programs.objects.count()
    # num_careers=Careers.objects.count()
    # num_skills=Skills.objects.count()
    num_careers=3
    num_skills=10
    return render(request, 'admin/dashboard.html',{
        'num_courses':num_courses,
        'num_careers':num_careers,
        'num_skills':num_skills
    })

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
    #skills=Skills.objects.all()
    skills = [
        "Python",
        "Java",
        "JavaScript",
        "SQL",
        "HTML/CSS",
        "C#",
        "C++",
        "Django",
        "React",
        "Node.js",
        "Git",
        "REST APIs",
        "Docker",
        "Kubernetes",
        "Linux/Unix",
        "AWS",
        "Azure",
        "Machine Learning",
        "Data Analysis",
        "Cloud Computing",
        "DevOps",
        "NoSQL Databases",
        "CI/CD",
        "Agile Methodologies",
        "Cybersecurity"
    ]
    # print (programs)
    # for program in programs:
    #     print(program) 

    return render(request,'admin/skills.html' ,{'skills':skills})



def fetch_onet_skillsrr(request):
    user ="zetech_ac_ke"
    password ="6448hxa"

    headers = {
        "Accept": "application/json"
    }

    try:
        # Step 1: Get occupations
        occ_url = "https://services.onetcenter.org/ws/online/occupations/"
        occ_response = requests.get(occ_url, auth=(user, password), headers=headers)

        if occ_response.status_code != 200:
            return JsonResponse({
                "error": "Failed to fetch occupations",
                "status": occ_response.status_code,
                "body": occ_response.text
            })

        # Access the list inside the dictionary
        json_data = occ_response.json()
        print("DEBUG:", json_data)  # Optional for debugging
        #occupations = json_data.get("occupation", [])[:1]  # Try 'occupation' or 'occupations'
        occupations = occ_response.json().get("occupation", []) 
        # Step 2: Fetch skills
        skills_data = []
        for occ in occupations:
            code = occ.get("code")
            title = occ.get("title")
            skill_url = f"https://services.onetcenter.org/ws/online/occupations/{code}/details/skills"
            skill_response = requests.get(skill_url, auth=(user, password), headers=headers)

            if skill_response.status_code == 200:
                skills = skill_response.json().get("skills", [])
                skills_data.append({"occupation": title, "skills": skills})
            else:
                skills_data.append({
                    "occupation": title,
                    "skills": [],
                    "error": "Could not fetch skills"
                })

        return JsonResponse({"data": skills_data})

    except Exception as e:
        return JsonResponse({"error": str(e)})

    
def edit_profile(request):
    return render(request,'admin/edit_profile.html')