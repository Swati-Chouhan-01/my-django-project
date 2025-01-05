
from django.urls import path
from . import views
from .import admin
urlpatterns = [
   path('',views.home,name='home'),
   path('about',views.about,name='about'),
   path('contact',views.contact,name='contact'),

   path('addinfo',views.add_info,name='addinfo'),
   path('updinfo/<id>',views.upd_info,name='updinfo'),
   path('showinfo/<id>',views.show_info,name='showinfo'),
   path('delinfo/<id>',views.del_info,name='delinfo'),


   path('addeducation/<id>',views.add_education,name='addeducation'),
   path('updeducation/<id>',views.upd_education,name='updeducation'),
   path('deleducation/<id>',views.del_education,name='deleducation'),

   path('addexperience/<id>',views.add_experience,name='addexperience'),
   path('updexperience/<id>',views.upd_experience,name='updexperience'),
   path('delexperience/<id>',views.del_experience,name='delexperience'),


   path('addproject/<id>',views.add_project,name='addproject'),
   path('updproject/<id>',views.upd_project,name='updproject'),
   path('delproject/<id>',views.del_project,name='delproject'),

   

   path('addachivements/<id>',views.add_achivements,name='addachivements'),
   path('updachivements/<id>',views.upd_achivements,name='updachivements'),
   path('delachivements/<id>',views.del_achivements,name='delachivements'),

   path('addtraining/<id>',views.add_training,name='addtraining'),
   path('updtraining/<id>',views.upd_training,name='updtraining'),
   path('deltraining/<id>',views.del_training,name='deltraining'),

 path('temp1/<id>',views.temp1,name='temp1'),
   path('temp2/<id>',views.temp2,name='temp2'),
   path('temp3/<id>',views.temp3,name='temp3'),
   path('temp4/<id>',views.temp4,name='temp4'),
   path('temp5/<id>',views.temp5,name='temp5'),
   path('temp6/<id>',views.temp6,name='temp6'),
   path('temp7/<id>',views.temp7,name='temp7'),
   path('temp8/<id>',views.temp8,name='temp8'),
   path('temp9/<id>',views.temp9,name='temp9'),
   path('temp10/<id>',views.temp10,name='temp10'),
   path('temp11/<id>',views.temp11,name='temp11'),
   path('temp12/<id>',views.temp12,name='temp12'),
   path('temp13/<id>',views.temp13,name='temp13'),
   

    path('signup',views.sign_up,name='signup'),
    path('login',views.log_in,name='login'),
    path('logout',views.log_out,name='logout'),

    path('resumelist',views.resume_list,name='resumelist'),
    path('temp/<id>',views.temp_view,name='temp'),
     path('alert',views.alert,name='alert'),


]