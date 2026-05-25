from csv import list_dialects
from django.contrib import admin
from student.models import student
from analytics.models import Predict
# Register your models here.
class studentDesing(admin.ModelAdmin):
    list_display = ['id', 'name', 'class_student', 'school', 'school_size', 'plan', 'family_income_per_month', 'status_family']

admin.site.register(student, studentDesing)