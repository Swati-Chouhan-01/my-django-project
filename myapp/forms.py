from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class CustomerRegistrationForm(UserCreationForm):
 password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
 password2 = forms.CharField(label='Confirm Password (Type again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
 email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
 class Meta:
  model = User
  fields = ['username', 'email', 'password1', 'password2']
  labels = {'email': 'Email'}
  widgets = {'username':forms.TextInput(attrs={'class':'form-control'})}

class LoginForm(AuthenticationForm):
 username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
 password = forms.CharField(label=("Password"), widget=forms.PasswordInput(attrs={'class':'form-control'}))


class candidateinfoForm(forms.ModelForm):
  candidate_name =forms.CharField(max_length=20,validators=[RegexValidator('[a-zA-Z][a-zA-Z]+[a-zA-Z]*$', message="Enter only alphabets")]),
  mobile =forms.CharField(max_length=10,validators=[RegexValidator('^[0-9]*$/', message="Enter only numbers")]),
  candidate_email=forms.EmailField(max_length=50,validators=[RegexValidator('^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$',message="Enter Valid E-mail")]),

  class Meta:
        model=CandidateInfo
        exclude = ['created_by']
        widgets={
                 'candidate_name':forms.TextInput(attrs={'class':'form-control'}),
                 'candidate_email':forms.EmailInput(attrs={'class':'form-control'}),
                 'date_of_birth':forms.DateInput(attrs={'class':'form-control','type':'date'}),
                 'mobile':forms.TextInput(attrs={'class':'form-control'}),
                 'address':forms.TextInput(attrs={'class':'form-control'}),
                 'my_website':forms.TextInput(attrs={'class':'form-control'}),
                 'linkedin_profile':forms.TextInput(attrs={'class':'form-control'}),
                 'facebook_profile':forms.TextInput(attrs={'class':'form-control'}),
                 'github_profile':forms.TextInput(attrs={'class':'form-control'}),
                 'twitter_profile':forms.TextInput(attrs={'class':'form-control'}),        
                 'language_known':forms.TextInput(attrs={'class':'form-control'}),
                 'objective':forms.TextInput(attrs={'class':'form-control'}),
                 'skills':forms.TextInput(attrs={'class':'form-control'}),
                 'interest':forms.TextInput(attrs={'class':'form-control'}),
                 'marital_status':forms.TextInput(attrs={'class':'form-control'}),
                 'nationality':forms.TextInput(attrs={'class':'form-control'}),
                #  'image':forms.ImageField(attrs={'class':'form-control'})
                   }
                  

class educationForm(forms.ModelForm):
    class Meta:
        model=Education
        exclude=['person']
        widgets={
                 'education_name':forms.TextInput(attrs={'class':'form-control'}),
                 'passing_year':forms.DateInput(attrs={'class':'form-control'}),
                 'board_or_university':forms.TextInput(attrs={'class':'form-control'}),
                 'percentage_or_grade':forms.TextInput(attrs={'class':'form-control'})
        }

class experienceForm(forms.ModelForm):
    class Meta:
        model=Experience
        exclude=['person']
        widgets={
                  'company_name':forms.TextInput(attrs={'class':'form-control'}),
                  'designation':forms.TextInput(attrs={'class':'form-control'}),
                  'start_date':forms.TextInput(attrs={'class':'form-control'}),
                  'end_date':forms.TextInput(attrs={'class':'form-control'}),
                  'description':forms.TextInput(attrs={'class':'form-control'})
          
          }

class projectForm(forms.ModelForm):
    class Meta:
        model=Project
        exclude=['person']
        widgets={
                  'project_title':forms.TextInput(attrs={'class':'form-control'}),
                  'description':forms.TextInput(attrs={'class':'form-control'}),
                  'skills_apply':forms.TextInput(attrs={'class':'form-control'}),
                  'duration_in_months': forms.NumberInput(attrs={'class':'form-control'})
          }



class achivementsForm(forms.ModelForm):
    class Meta:
        model=Achivements
        exclude=['person']
        widgets={
                  'title':forms.TextInput(attrs={'class':'form-control'}),
                  'description':forms.TextInput(attrs={'class':'form-control'})
         }
        
class trainingForm(forms.ModelForm):
    class Meta:
        model=Training
        exclude=['person']
        widgets={
                  'company_or_institute_name':forms.TextInput(attrs={'class':'form-control'}),
                  'learn_skills':forms.TextInput(attrs={'class':'form-control'}),
                  'duration_in_month':forms.NumberInput(attrs={'class':'form-control'}),
                  'description':forms.TextInput(attrs={'class':'form-control'})
         }
        