from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError, DataError
from student.models import student as Student

# =========================
# Student Fields
# =========================
# แยก field ที่ "บังคับกรอก" ออกจาก field ที่ "ไม่บังคับ" (ex1-ex20)
# เพื่อป้องกันบั๊กที่ผู้ใช้กรอกข้อมูลจริงครบแล้ว แต่ระบบเด้งเตือนว่า
# "กรอกไม่ครบ" เพราะไปนับรวม field เสริมที่ไม่จำเป็นต้องกรอกด้วย
REQUIRED_FIELDS = [
    'gender', 'name', 'class_student', 'school',
    'short', 'school_size', 'plan', 'round_apply',
    'GPA', 'grade_maths', 'grade_science',
    'grade_english', 'skillcomputer',
    'traincomputer', 'write_program',
    'trainprogram', 'Other_skills',
    'want_to_develop', 'family_income_per_month',
    'status_family',
    'which_channel_do_you_know',
    'why_did_you_choose_to_study',
]

OPTIONAL_FIELDS = [f'ex{i}' for i in range(1, 21)]

ALL_FIELDS = REQUIRED_FIELDS + OPTIONAL_FIELDS


# =========================
# Views
# =========================
def home(request):
    return render(request, 'home.html')


def form(request):
    return render(request, 'form.html')


def addstudent(request):
    if request.method != "POST":
        return redirect('formstudent')

    data = {field: request.POST.get(field, '').strip() for field in ALL_FIELDS}

    # ตรวจสอบเฉพาะ field ที่บังคับกรอกจริง ๆ
    missing_fields = [field for field in REQUIRED_FIELDS if not data[field]]
    if missing_fields:
        messages.warning(request, "กรุณากรอกข้อมูลให้ครบทุกช่องที่จำเป็น")
        return redirect('formstudent')

    # ครอบ try/except กัน error ตอนบันทึกจริง เช่น ค่าที่กรอกไม่ตรง type
    # ของ field ในโมเดล (เช่น GPA ไม่ใช่ตัวเลข) ซึ่งถ้าไม่ครอบไว้
    # จะทำให้เว็บ error 500 ทันทีเมื่อใช้งานจริง
    try:
        Student.objects.create(**data)
    except (IntegrityError, DataError, ValueError):
        messages.error(request, "เกิดข้อผิดพลาดในการบันทึกข้อมูล กรุณาตรวจสอบข้อมูลที่กรอกอีกครั้ง")
        return redirect('formstudent')

    messages.success(request, "บันทึกข้อมูลเรียบร้อยแล้ว")
    return redirect('formstudent')