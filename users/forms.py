from django import forms

from django.contrib.auth import authenticate  
from .models import Users

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('first_name','last_name','surname', 'email','role')
        widgets={
            'role':forms.Select(attrs={'class': 'form-control'}),
        }

class EmailAuthenticationForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if email and password:
            self.user = authenticate(username=email, password=password)
            if self.user is None:
                raise forms.ValidationError("Invalid email or password")
        return self.cleaned_data
    
    def get_user(self):
        return self.user if hasattr(self, 'user') else None
   
