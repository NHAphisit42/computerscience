from django.shortcuts import render, redirect
from django.contrib import messages
from student.models import student


# =========================
# Views
# =========================
def home(request):
    return render(request, 'home.html')


def form(request):
    return render(request, 'form.html')


# =========================
# Student Fields
# =========================
FIELDS = [
    'gender', 'name', 'class_student', 'school',
    'short', 'school_size', 'plan', 'round_apply',
    'GPA', 'grade_maths', 'grade_science',
    'grade_english', 'skillcomputer',
    'traincomputer', 'write_program',
    'trainprogram', 'Other_skills',
    'want_to_develop', 'family_income_per_month',
    'status_family',
    'which_channel_do_you_know',
    'why_did_you_choose_to_study'
] + [f'ex{i}' for i in range(1, 21)]


# =========================
# Add Student
# =========================
def addstudent(request):

    if request.method != "POST":
        return redirect('formstudent')

    # ดึงข้อมูลทั้งหมดอัตโนมัติ
    data = {field: request.POST.get(field, '').strip() for field in FIELDS}

    # ตรวจสอบข้อมูลว่าง
    empty_fields = [key for key, value in data.items() if not value]

    if empty_fields:
        messages.warning(request, "กรุณากรอกข้อมูลให้ครบ")
        return redirect('formstudent')

    # บันทึกข้อมูล
    student.objects.create(**data)

    messages.success(request, "กรอกข้อมูลครบถ้วน")
    return redirect('formstudent')