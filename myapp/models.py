from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()
import datetime
from django.core.validators import RegexValidator



# Create your models here.

year_choice=[(r,r) for r in range(1984,datetime.date.today().year+1)]

class CandidateInfo(models.Model):
    candidate_name=models.CharField(max_length=50,validators=[RegexValidator("[a-zA-Z][a-zA-Z]+[a-zA-Z]$",message="Enter only Alphabets")])
    candidate_email=models.EmailField(max_length=50,validators=[RegexValidator("^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$",message="Enter Valid E-mail")])
    date_of_birth=models.DateField()
    mobile=models.CharField(max_length=10, validators=[RegexValidator("^[0-9]*$",message="Enter only Numbers")])
    address=models.CharField(max_length=255)
    my_website=models.CharField(max_length=255,null='True',blank='True')
    linkedin_profile=models.CharField(max_length=50,null='True',blank='True')
    facebook_profile=models.CharField(max_length=50,null='True',blank='True')
    github_profile=models.CharField(max_length=50,null='True',blank='True')
    twitter_profile=models.CharField(max_length=50,null='True',blank='True')
    objective=models.CharField( max_length=255,null='True',blank='True')
    language_known=models.CharField(max_length=50,null='True', blank='True')
    skills=models.CharField(max_length=255,null='True', blank='True')
    interest=models.CharField(max_length=255,null='True' ,blank='True')
    marital_status=models.CharField(max_length=255,null='True',blank='True')
    nationality=models.CharField(max_length=255,null='True',blank='True')
    image=models.ImageField(upload_to='img',null='True' ,blank='True')
    created_by= models.ForeignKey(User, on_delete=models.CASCADE,default=User)

    def __str__(self):
        return self.candidate_name


class Education(models.Model):
    person=models.ForeignKey(CandidateInfo,on_delete=models.CASCADE)
    education_name=models.CharField(max_length=50)
    passing_year=models.IntegerField(choices=year_choice)
    board_or_university=models.CharField(max_length=200)
    percentage_or_grade=models.CharField(max_length=50)
    
    def __str__(self):
        return self.education_name
    
class Experience(models.Model):
    person=models.ForeignKey(CandidateInfo,on_delete=models.CASCADE)
    company_name=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)
    start_date=models.IntegerField(choices=year_choice)
    end_date=models.IntegerField(choices=year_choice)
    description=models.CharField(max_length=255)


    def __str__(self):
        return self.designation
    
class Project(models.Model):
    person=models.ForeignKey(CandidateInfo,on_delete=models.CASCADE)
    project_title=models.CharField(max_length=50)
    description=models.CharField(max_length=255)
    skills_apply=models.CharField(max_length=50)
    duration_in_months=models.IntegerField()


    def __str__(self):
        return self.project_title
    
class Achivements(models.Model):
    person=models.ForeignKey(CandidateInfo,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=255)
     
    def __str__(self):
        return self.title
    
class Training(models.Model):
    person=models.ForeignKey(CandidateInfo,on_delete=models.CASCADE)
    company_or_institute_name=models.CharField(max_length=50)
    learn_skills=models.CharField(max_length=50)
    duration_in_month=models.IntegerField()
    description=models.CharField(max_length=255)
     
    def __str__(self):
        return self.company_or_institute_name

class Contact(models.Model):
    name=models.CharField(max_length=20,validators=[RegexValidator("[a-zA-Z\s]+",message="Enter only Alphabets")])
    email=models.EmailField(max_length=20,validators=[RegexValidator("[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,4}$",message="Enter Valid E-mail")])
    subject=models.CharField(max_length=255)
    message=models.CharField(max_length=255)

    def __str__(self):
        return self.name