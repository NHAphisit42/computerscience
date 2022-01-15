from django.contrib import admin
from student.models import student
# Register your models here.
class studentDesing(admin.ModelAdmin):
    list_display = ['id', 'gender', 'name', 'sophomore_student', 'school', 'plan']

admin.site.register(student, studentDesing)