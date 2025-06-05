from django.urls import path
from .import views

urlpatterns=[
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('programs/', views.programs_view, name='programs'),
    path('jobs/', views.jobs, name='jobs'),
    path('skills/', views.skills, name='skills'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    
]

