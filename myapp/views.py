


from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
# Create your views here.


def sign_up(request): 
    if request.method == 'POST':
        myform = CustomerRegistrationForm(request.POST)
        if myform.is_valid():
            myform.save()
            msgs='Congratulations!! Registered Successfully.'
            myform = CustomerRegistrationForm()
            return render(request,'signup.html',{'myform':myform,'msgs':msgs})
        else:
            msge= 'Create Strong Password'
            myform = CustomerRegistrationForm()
            return render(request,'signup.html',{'myform':myform,'msge':msge})   
    else:
        myform = CustomerRegistrationForm()
        return render(request,'signup.html',{'myform':myform})


def log_in(request):
    if request.method == "POST":
        myform = LoginForm(request=request,data=request.POST)
        if myform.is_valid():
            uname=myform.cleaned_data['username']
            upass= myform.cleaned_data['password']

            request.session['uname']=uname
            user = authenticate(username=uname,password=upass)
            login(request,user)
        
            return redirect('home')
        else:
            msg = "username or password is incorrect"
            myform = LoginForm()
            return render(request,'login.html',{'myform':myform,'msge':msg})    
    else:
        myform = LoginForm()
        return render(request,'login.html',{'myform':myform})




def log_out(request):
    logout(request)
    return redirect('login')        

def resume_list(request):
    
    username=request.user
    data = CandidateInfo.objects.filter(created_by = username)
    return render(request,'resume_list.html',{'data':data})

def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def alert(request):
    return render(request,'alert.html')


def contact(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        c1=Contact(name=name,email=email,subject=subject,message=message)
        c1.save()
        return render(request,'contact.html')
    else:
        return render(request,'contact.html')


def add_info(request):
    if request.method == 'POST':
     
       infoform=candidateinfoForm(request.POST,request.FILES)
       if infoform.is_valid():
         candidate_name=infoform.cleaned_data["candidate_name"]
         candidate_email=infoform.cleaned_data["candidate_email"]
         date_of_birth=infoform.cleaned_data["date_of_birth"]
         mobile=infoform.cleaned_data["mobile"]
         address=infoform.cleaned_data["address"]
         my_website=infoform.cleaned_data["my_website"]
         linkedin_profile=infoform.cleaned_data["linkedin_profile"]
         facebook_profile=infoform.cleaned_data["facebook_profile"]
         github_profile=infoform.cleaned_data["github_profile"]
         twitter_profile=infoform.cleaned_data["twitter_profile"]
         objective=infoform.cleaned_data["objective"]
         language_known=infoform.cleaned_data["language_known"]
         skills=infoform.cleaned_data["skills"]
         interest=infoform.cleaned_data["interest"]
         marital_status=infoform.cleaned_data["marital_status"]
         nationality=infoform.cleaned_data["nationality"]
         image=infoform.cleaned_data["image"]
         created_by=request.user
       
         info=CandidateInfo(candidate_name=candidate_name,candidate_email=candidate_email, date_of_birth=date_of_birth, mobile= mobile,address=address, my_website= my_website, linkedin_profile= linkedin_profile,facebook_profile=facebook_profile,github_profile=github_profile,twitter_profile=twitter_profile,objective=objective,image= image,language_known=language_known,skills=skills,interest=interest,marital_status=marital_status,nationality=nationality,created_by=created_by)
         info.save()
         messages.success(request,"Formsubmitted")
         return redirect('addeducation', id=info.id)
       
       return render(request,'addinfo.html',{'infoform':infoform })
  
            
       
    else:
        infoform=candidateinfoForm()
        return render(request,'addinfo.html',{'infoform':infoform })
    
def upd_info(request,id):
    if request.method == 'POST':
       obj= CandidateInfo.objects.get(id=id)
       infoform=candidateinfoForm(request.POST,request.FILES,instance=obj)
       if infoform.is_valid():
            infoform.save()
            return redirect('showinfo', id=obj.id)
            
       else:
             return redirect('alert')
    else:
        obj= CandidateInfo.objects.get(id=id)
        obj1=CandidateInfo.objects.filter(id=id) 
        infoform=candidateinfoForm(instance=obj)
        return render(request,'showinfo.html',{'infoform':infoform,'data':obj1,'id':obj.id})
    
def show_info(request,id):
    obj=CandidateInfo.objects.filter(id=id)    
    return render(request, 'showinfo.html',{'data':obj, 'id':id})

def del_info(request,id):
    obj= CandidateInfo.objects.get(id=id)
    obj.delete()
    return redirect('resumelist')
    
def add_education(request,id):
    if request.method=='POST':

        edform=educationForm(request.POST)
        if edform.is_valid():
            person=CandidateInfo.objects.get(id=id)
            education_name=edform.cleaned_data["education_name"]
            passing_year=edform.cleaned_data["passing_year"]
            board_or_university=edform.cleaned_data["board_or_university"]
            percentage_or_grade=edform.cleaned_data["percentage_or_grade"]
            ed=Education(person=person,education_name=education_name,passing_year=passing_year,board_or_university=board_or_university,percentage_or_grade=percentage_or_grade)
            ed.save()
            return  redirect('addeducation',id=id)
        else:
            return redirect('alert')
   
    else:
          person=CandidateInfo.objects.get(id=id)
          education=Education.objects.filter(person=person)
          edform=educationForm()
          return render(request,'addeducation.html',{'edform':edform,'id':id,'data':education})
    
def upd_education(request,id):
    if request.method == 'POST':
       obj= Education.objects.get(id=id)
       edform=educationForm(request.POST,instance=obj)
       if edform.is_valid():
            edform.save()
            return redirect('addeducation', id=obj.person.id)
       else:
             return redirect('alert')
    else:
        obj= Education.objects.get(id=id)
        person=CandidateInfo.objects.get(id=obj.person.id)
        education=Education.objects.filter(person=person)
        edform=educationForm(instance=obj)
        return render(request,'addeducation.html',{'edform':edform,'id':obj.person,'data':education})

def del_education(request,id):
    obj= Education.objects.get(id=id)
    obj.delete()
    return redirect('addeducation',id=obj.person.id)

    

    
def add_experience(request,id):
    if request.method == 'POST':
        expform=experienceForm(request.POST)
        if expform.is_valid():

            person=CandidateInfo.objects.get(id=id)
            company_name=expform.cleaned_data["company_name"]
            designation=expform.cleaned_data["designation"]
            start_date=expform.cleaned_data["start_date"]
            end_date=expform.cleaned_data["end_date"]
            description=expform.cleaned_data["description"]
            exp=Experience(person=person,company_name=company_name, designation= designation,start_date=start_date,end_date=end_date,description=description)
            exp.save()
            return  redirect('addexperience',id=id)
        else:
             return redirect('alert')
   
    else:
          person=CandidateInfo.objects.get(id=id)
          experience=Experience.objects.filter(person=person)
          expform=experienceForm()
          return render(request,'addexperience.html',{'expform':expform,'id':id,'data':experience})
                
def upd_experience(request,id):
    if request.method == 'POST':
       obj= Experience.objects.get(id=id)
       expform=experienceForm(request.POST,instance=obj)
       if expform.is_valid():
            expform.save()
            return redirect('addexperience', id=obj.person.id)
            
       else:
            return redirect('alert')
    else:
        obj= Experience.objects.get(id=id)
        person=CandidateInfo.objects.get(id=obj.person.id)
        experience=Experience.objects.filter(person=person)
        expform=experienceForm(instance=obj)
        return render(request,'addexperience.html',{'expform':expform,'id':obj.person,'data':experience})
    
def del_experience(request,id):
    obj= Experience.objects.get(id=id)
    obj.delete()
    return redirect('addexperience',id=obj.person.id)    


    
def add_project(request,id):
    if request.method=='POST':
        proform=projectForm(request.POST)
        if proform.is_valid():
            person=CandidateInfo.objects.get(id=id)
            project_title=proform.cleaned_data["project_title"]
            description=proform.cleaned_data["description"]
            skills_apply=proform.cleaned_data["skills_apply"]
            duration_in_months=proform.cleaned_data["duration_in_months"]
            pro=Project(person=person,project_title=project_title,description=description,skills_apply=skills_apply,duration_in_months=duration_in_months)
            pro.save()
            return  redirect('addproject' , id=id)
        else:
             return redirect('alert')
   
    else:
          person=CandidateInfo.objects.get(id=id)
          project=Project.objects.filter(person=person)
          proform=projectForm()
          return render(request,'addproject.html',{'proform':proform,'id':id,'data':project})
                
def upd_project(request,id):
    if request.method == 'POST':
       obj= Project.objects.get(id=id)
       proform=projectForm(request.POST,instance=obj)
       if proform.is_valid():
            proform.save()
            return  redirect('addproject' , id=obj.person.id)
            
       else:
             return redirect('alert')
    else:
        obj= Project.objects.get(id=id)
        person=CandidateInfo.objects.get(id=obj.person.id)
        project=Project.objects.filter(person=person)
        proform=projectForm(instance=obj)
        return render(request,'addproject.html',{'proform':proform,'id':obj.person,'data':project})
    
def del_project(request,id):
    obj= Project.objects.get(id=id)
    obj.delete()
    return redirect('addproject',id=obj.person.id)     

           
def add_achivements(request,id):
    if request.method=='POST':
        achivform=achivementsForm(request.POST)
        if achivform.is_valid():
            person=CandidateInfo.objects.get(id=id)
            title=achivform.cleaned_data["title"]
            description=achivform.cleaned_data["description"]
            achiv=Achivements(person=person,title=title,description=description)
            achiv.save()
            return redirect('addachivements', id=id)
        else:
             return redirect('alert')
   
    else:
          person=CandidateInfo.objects.get(id=id)
          achivements=Achivements.objects.filter(person=person)
          achivform=achivementsForm()
          return render(request,'addachivements.html',{'achivform':achivform,'id':id,'data':achivements})
                
           
def upd_achivements(request,id):
    if request.method == 'POST':
       obj= Achivements.objects.get(id=id)
       achivform=achivementsForm(request.POST,instance=obj)
       if achivform.is_valid():
            achivform.save()
            return redirect('addachivements', id=obj.person.id)
            
       else:
             return redirect('alert')
    else:
        obj= Achivements.objects.get(id=id)
        person=CandidateInfo.objects.get(id=obj.person.id)
        achivements=Achivements.objects.filter(person=person)
        achivform=achivementsForm(instance=obj)
        return render(request,'addachivements.html',{'achivform':achivform,'id':obj.person,'data':achivements})
    
def del_achivements(request,id):
    obj= Achivements.objects.get(id=id)
    obj.delete()
    return redirect('addachivements',id=obj.person.id)     
    

def add_training(request,id):
    if request.method=='POST':
        trngform=trainingForm(request.POST)
        if trngform.is_valid():
            person=CandidateInfo.objects.get(id=id)
            company_or_institute_name=trngform.cleaned_data["company_or_institute_name"]
            learn_skills=trngform.cleaned_data["learn_skills"]
            duration_in_month=trngform.cleaned_data["duration_in_month"]
            description=trngform.cleaned_data["description"]
            trng=Training(person=person,company_or_institute_name=company_or_institute_name,learn_skills=learn_skills,duration_in_month=duration_in_month,description=description)
            trng.save()
            return redirect('addtraining', id=id)
        else:
             return redirect('alert')
   
    else:
          person=CandidateInfo.objects.get(id=id)
          training=Training.objects.filter(person=person)
          trngform=trainingForm()
          return render(request,'addtraining.html',{'trngform':trngform,'id':id,'data':training})
                
           
def upd_training(request,id):
    if request.method == 'POST':
       obj= Training.objects.get(id=id)
       trngform=trainingForm(request.POST,instance=obj)
       if trngform.is_valid():
            trngform.save()
            return redirect('addtraining', id=obj.person.id)
            
       else:
             return redirect('alert')
    else:
        obj=Training.objects.get(id=id)
        person=CandidateInfo.objects.get(id=obj.person.id)
        training=Training.objects.filter(person=person)
        trngform=trainingForm(instance=obj)
        return render(request,'addtraining.html',{'trngform':trngform,'id':obj.person,'data':training})
    
def del_training(request,id):
    obj= Training.objects.get(id=id)
    obj.delete()
    return redirect('addtraining',id=obj.person.id)     
    

def temp_view(request,id):
    return render(request,'temp.html',{'id':id})

def temp1(request,id):
    pdata = CandidateInfo.objects.get(id=id)
    edata = Education.objects.filter(person=pdata)
    exdata = Experience.objects.filter(person=pdata)
    prdata = Project.objects.filter(person=pdata)
    adata = Achivements.objects.filter(person=pdata)
    tdata=Training.objects.filter(person=pdata)
    context={'pdata':pdata,'edata':edata,'exdata':exdata,'prdata':prdata,'adata':adata,'tdata':tdata}

    return render(request,'temp1.html',context)
    

def temp2(request,id):
    pdata = CandidateInfo.objects.get(id=id)
    edata = Education.objects.filter(person=pdata)
    exdata = Experience.objects.filter(person=pdata)
    prdata = Project.objects.filter(person=pdata)
    adata = Achivements.objects.filter(person=pdata)
    tdata=Training.objects.filter(person=pdata)

    context={'pdata':pdata,'edata':edata,'exdata':exdata,'prdata':prdata,'adata':adata,'tdata':tdata}



    return render(request,'temp2.html',context)

def temp3(request,id):
    pdata = CandidateInfo.objects.get(id=id)
    edata = Education.objects.filter(person=pdata)
    exdata = Experience.objects.filter(person=pdata)
    prdata = Project.objects.filter(person=pdata)
    adata = Achivements.objects.filter(person=pdata)
    tdata=Training.objects.filter(person=pdata)

    context={'pdata':pdata,'edata':edata,'exdata':exdata,'prdata':prdata,'adata':adata,'tdata':tdata}

    return render(request,'temp3.html',context)

def temp4(request,id):
    pdata = CandidateInfo.objects.get(id=id)
    edata = Education.objects.filter(person=pdata)
    exdata = Experience.objects.filter(person=pdata)
    prdata = Project.objects.filter(person=pdata)
    adata = Achivements.objects.filter(person=pdata)
    tdata=Training.objects.filter(person=pdata)

    context={'pdata':pdata,'edata':edata,'exdata':exdata,'prdata':prdata,'adata':adata,'tdata':tdata}

    return render(request,'temp4.html',context)

def temp5(request,id):
    pdata = CandidateInfo.objects.get(id=id)
    edata = Education.objects.filter(person=pdata)
    exdata = Experience.objects.filter(person=pdata)
    prdata = Project.objects.filter(person=pdata)
    adata = Achivements.objects.filter(person=pdata)
    tdata=Training.objects.filter(person=pdata)

    context={'pdata':pdata,'edata':edata,'exdata':exdata,'prdata':prdata,'adata':adata,'tdata':tdata}

    return render(request,'temp5.html',context)

def temp6(request,id):
    pdata = CandidateInfo.objects.get(id=id)
    edata = Education.objects.filter(person=pdata)
    exdata = Experience.objects.filter(person=pdata)
    prdata = Project.objects.filter(person=pdata)
    adata = Achivements.objects.filter(person=pdata)
    tdata=Training.objects.filter(person=pdata)

    context={'pdata':pdata,'edata':edata,'exdata':exdata,'prdata':prdata,'adata':adata,'tdata':tdata}

    return render(request,'temp6.html',context)
def temp7(request,id):
    pdata = CandidateInfo.objects.get(id=id)
    edata = Education.objects.filter(person=pdata)
    exdata = Experience.objects.filter(person=pdata)
    prdata = Project.objects.filter(person=pdata)
    adata = Achivements.objects.filter(person=pdata)
    tdata=Training.objects.filter(person=pdata)

    context={'pdata':pdata,'edata':edata,'exdata':exdata,'prdata':prdata,'adata':adata,'tdata':tdata}

    return render(request,'temp7.html',context)

def temp8(request,id):
    pdata = CandidateInfo.objects.get(id=id)
    edata = Education.objects.filter(person=pdata)
    exdata = Experience.objects.filter(person=pdata)
    prdata = Project.objects.filter(person=pdata)
    adata = Achivements.objects.filter(person=pdata)
    tdata=Training.objects.filter(person=pdata)

    context={'pdata':pdata,'edata':edata,'exdata':exdata,'prdata':prdata,'adata':adata,'tdata':tdata}

    return render(request,'temp8.html',context)

def temp9(request,id):
    pdata = CandidateInfo.objects.get(id=id)
    edata = Education.objects.filter(person=pdata)
    exdata = Experience.objects.filter(person=pdata)
    prdata = Project.objects.filter(person=pdata)
    adata = Achivements.objects.filter(person=pdata)
    tdata=Training.objects.filter(person=pdata)

    context={'pdata':pdata,'edata':edata,'exdata':exdata,'prdata':prdata,'adata':adata,'tdata':tdata}

    return render(request,'temp9.html',context)

def temp10(request,id):
    pdata = CandidateInfo.objects.get(id=id)
    edata = Education.objects.filter(person=pdata)
    exdata = Experience.objects.filter(person=pdata)
    prdata = Project.objects.filter(person=pdata)
    adata = Achivements.objects.filter(person=pdata)
    tdata=Training.objects.filter(person=pdata)

    context={'pdata':pdata,'edata':edata,'exdata':exdata,'prdata':prdata,'adata':adata,'tdata':tdata}

    return render(request,'temp10.html',context)

def temp11(request,id):
    pdata = CandidateInfo.objects.get(id=id)
    edata = Education.objects.filter(person=pdata)
    exdata = Experience.objects.filter(person=pdata)
    prdata = Project.objects.filter(person=pdata)
    adata = Achivements.objects.filter(person=pdata)
    tdata=Training.objects.filter(person=pdata)

    context={'pdata':pdata,'edata':edata,'exdata':exdata,'prdata':prdata,'adata':adata,'tdata':tdata}

    return render(request,'temp11.html',context)


def temp12(request,id):
    pdata = CandidateInfo.objects.get(id=id)
    edata = Education.objects.filter(person=pdata)
    exdata = Experience.objects.filter(person=pdata)
    prdata = Project.objects.filter(person=pdata)
    adata = Achivements.objects.filter(person=pdata)
    tdata=Training.objects.filter(person=pdata)

    context={'pdata':pdata,'edata':edata,'exdata':exdata,'prdata':prdata,'adata':adata,'tdata':tdata}

    return render(request,'temp12.html',context)


def temp13(request,id):
    pdata = CandidateInfo.objects.get(id=id)
    edata = Education.objects.filter(person=pdata)
    exdata = Experience.objects.filter(person=pdata)
    prdata = Project.objects.filter(person=pdata)
    adata = Achivements.objects.filter(person=pdata)
    tdata=Training.objects.filter(person=pdata)

    context={'pdata':pdata,'edata':edata,'exdata':exdata,'prdata':prdata,'adata':adata,'tdata':tdata}

    return render(request,'temp13.html',context)









                









        
