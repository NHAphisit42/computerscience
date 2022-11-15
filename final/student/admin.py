from csv import list_dialects
from django.contrib import admin
from student.models import student, School, Round_apply, Plan, Eduction
# Register your models here.
class studentDesing(admin.ModelAdmin):
    list_display = ['id', 'gender', 'name', 'class_student', 'school', 'plan']

class schoolDesing(admin.ModelAdmin):
    list_display = ['id', 'name_school', 'size_school', 'zone_school', 'district_school', 'province_school', 'Latitude', 'Longitude']

class round_applyDesing(admin.ModelAdmin):
    list_display = ['id', 'round_apply_name']

class educationDesing(admin.ModelAdmin):
    list_display = ['id', 'education_name']

class planDesing(admin.ModelAdmin):
    list_display = ['id', 'plan_name']

admin.site.register(student, studentDesing)
admin.site.register(School, schoolDesing)
admin.site.register(Plan, planDesing)
admin.site.register(Eduction, educationDesing)
admin.site.register(Round_apply, round_applyDesing)