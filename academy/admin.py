from django.contrib import admin
from academy.models import Career, Student, Subject, SubjectByStudent

class CareerAdmin(admin.ModelAdmin):
    list_display = ["name", "duration"]
    list_display_links = ["name"]

class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "surname", "dni", "sex", "career", "year", "liability"]
    list_display_links = ["name", "surname", "dni"]
  
class SubjectAdmin(admin.ModelAdmin):
    list_display = ["subject_name"]

class SubjectByStudentAdmin(admin.ModelAdmin):
    list_display = ["student", "name", "date"]

admin.site.register(Career, CareerAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(SubjectByStudent, SubjectByStudentAdmin)