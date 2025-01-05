from django.contrib import admin
from .models import *
# Register your models here.

class CandidateinfoAdmin(admin.ModelAdmin):
    list_display=['candidate_name','candidate_email','date_of_birth','mobile','address','my_website','linkedin_profile','facebook_profile','github_profile','twitter_profile','objective','language_known','skills','interest','marital_status', 'nationality','image','created_by']

    def get_queryset(self,request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:  
            return qs
        return qs.filter(User_Name=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "created_by":
            kwargs["queryset"]= User.objects.filter(username = request.user.username)  # type: ignore
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(CandidateInfo,CandidateinfoAdmin)

class EducationAdmin(admin.ModelAdmin):
    list_display=['person','education_name','passing_year','board_or_university','percentage_or_grade']

admin.site.register(Education,EducationAdmin)

class ExperienceAdmin(admin.ModelAdmin):
    list_display=['person','company_name','designation','start_date','end_date','description']

admin.site.register(Experience,ExperienceAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display=['person','project_title','description','skills_apply','duration_in_months']

admin.site.register(Project,ProjectAdmin)

class AchivementsAdmin(admin.ModelAdmin):
    list_display=['person','title','description']
    
admin.site.register(Achivements,AchivementsAdmin)

class TrainingAdmin(admin.ModelAdmin):
    list_display=['person','company_or_institute_name','learn_skills','duration_in_month','description']
    
admin.site.register(Training,TrainingAdmin)

admin.site.register(Contact)

admin.site.index_title="Resume Builder"
admin.site.site_header="Resume Builder"
admin.site.site_title="Resume Builder"  


    

    