import string
import random
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from .forms import CustomUserCreationForm, EmailAuthenticationForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings



def generate_password(length=10):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def signup_view(request):
    if(request.method=='POST'):
        form=CustomUserCreationForm(request.POST)
        if(form.is_valid()):
            user=form.save(commit=False)
           # password= generate_password()
            password='Zustaff@123'
            user.set_password(password)
            user.save()
            # send_mail(
            #     'Your EduNova Account Password',
            #     f'Hello {user.first_name},\n\nYour account has been created. Your password is: {password}\n\nPlease log in and change your password.',
            #     settings.DEFAULT_FROM_EMAIL,
            #     [user.email],
            #     fail_silently=False,
            # )
            # login(request,user)

            print(f"Registered email: {user.email} | Password: {password}")
            messages.success(request,'Account created successfully')
            return redirect('login')
        else:
            print(form.errors)
            messages.error(request,'Error creating account. Please correct the errors below.')
            form=CustomUserCreationForm(request.POST)
    else:
        form=CustomUserCreationForm()
    return render(request,'users/signup.html',{'form':form})
    
def login_view(request):
    if(request.method=='POST'):
        form=EmailAuthenticationForm(request.POST)
        if form.is_valid():
            login(request,form.get_user())
            return  redirect('dashboard')
        else:
            print(form.errors)
    else:
        form=EmailAuthenticationForm()
    return render(request,'users/login.html',{'form':form})
        
def logout_view(request):
    if(request.method=='POST'):
        logout(request)
    return redirect('login')