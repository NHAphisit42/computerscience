from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings
from joblib import load
import os

from student.models import student

# =========================
# ML Models
# =========================
ML_DIR = os.path.join(settings.BASE_DIR, 'analytics', 'ML')
model_logistic = load(os.path.join(ML_DIR, 'Logistics.joblib'))
model_cluster = load(os.path.join(ML_DIR, 'clustering.joblib'))

# =========================
# Constants
# =========================
EX_FIELDS = [f'ex{i}' for i in range(1, 21)]

STUDENT_FIELDS = [
    'gender', 'name', 'class_student', 'school',
    'school_size', 'short', 'plan', 'round_apply',
    'GPA', 'grade_maths', 'grade_science',
    'grade_english', 'skillcomputer',
    'traincomputer', 'write_program',
    'trainprogram', 'Other_skills',
    'want_to_develop', 'family_income_per_month',
    'status_family',
    'which_channel_do_you_know',
    'why_did_you_choose_to_study'
] + EX_FIELDS

CLUSTER_TEXT = {
    0: "เน้นปูพื้นฐานเขียนโปรแกรมและภาษา",
    1: "ทบทวนพื้นฐานเขียนโปรแกรมและคำนวณ",
    2: "ปูพื้นฐานเขียนโปรแกรมและคำนวณ",
}


# =========================
# Utility Functions
# =========================
def get_growthmindset(score):
    if 45 <= score <= 60:
        return "Strong Growth Mindset"
    elif 34 <= score <= 44:
        return "Growth Mindset with some Fixed Mindset"
    elif 21 <= score <= 33:
        return "Fixed Mindset with some Growth Mindset"
    return "Strong Fixed Mindset"


def get_prediction(std):
    data = [[
        student.school_size_no(std),
        student.plan_no(std),
        student.round_apply_no(std),
        float(std.GPA or 0),
        student.write_program_no(std),
        student.trainprogram_no(std),
        student.family_income_per_month_no(std),
        student.status_family_no(std)
    ]]
    result = model_logistic.predict(data)[0]
    return "ผ่าน" if result else "ไม่ผ่าน"


def get_cluster(std):
    data = [[
        float(std.GPA or 0),
        student.plan_no(std),
        student.write_program_no(std)
    ]]
    result = model_cluster.predict(data)[0]
    return CLUSTER_TEXT.get(result, "ไม่พบข้อมูล")


def _save_student_fields(std, post_data):
    """อัปเดตฟิลด์ของ student จาก POST data อย่างปลอดภัย"""
    for field in STUDENT_FIELDS:
        if field in post_data:
            setattr(std, field, post_data.get(field))
    std.save()


# =========================
# Views
# =========================
@login_required(login_url='login_backend')
def home_backend(request):
    std = student.objects.only('id', 'name', 'class_student')
    return render(request, 'home_backend.html', {'std': std})


@login_required(login_url='login_backend')
def table_backend(request):
    std = student.objects.all()
    return render(request, 'student_table_backend.html', {
        'std': std,
        'count': std.count()
    })


@login_required(login_url='login_backend')
def remove(request, id):
    if request.method != "POST":
        messages.error(request, "คำขอไม่ถูกต้อง")
        return redirect('table_backend')

    get_object_or_404(student, id=id).delete()
    messages.success(request, "ลบข้อมูลเรียบร้อยแล้ว")
    return redirect('table_backend')


@login_required(login_url='login_backend')
def studentdetail(request, id):
    std = get_object_or_404(student, id=id)

    if request.method == "POST":
        _save_student_fields(std, request.POST)
        messages.success(request, "แก้ไขข้อมูลเรียบร้อยแล้ว")
        return redirect('table_backend')

    total = 0
    for f in EX_FIELDS:
        val = getattr(std, f, 0)
        try:
            total += int(val)
        except (TypeError, ValueError):
            pass

    return render(request, 'studentdetail.html', {
        'std': std,
        'sum': get_growthmindset(total)
    })


def login_backend(request):
    if request.user.is_authenticated:
        return redirect('home_backend')
    return render(request, 'login_backend.html')


@login_required(login_url='login_backend')
def logout_backend(request):
    logout(request)
    return redirect('login_backend')


def register_backend(request):
    return render(request, 'register_backend.html')


@login_required(login_url='login_backend')
def predictive(request):
    return render(request, 'predictive.html')


@login_required(login_url='login_backend')
def student_list(request):
    if request.method != "POST":
        return redirect('predictive')

    class_std = request.POST.get('class_student')
    if not class_std:
        messages.error(request, "กรุณาป้อนข้อมูลให้ครบ")
        return redirect('predictive')

    sd = student.objects.filter(class_student=class_std)
    return render(request, 'predictive.html', {'sd': sd})


@login_required(login_url='login_backend')
def result(request):
    if request.method != "POST":
        return redirect('predictive')

    ids = request.POST.getlist('checkbox[]')
    if not ids:
        messages.error(request, "กรุณาเลือกนักเรียนอย่างน้อย 1 คน")
        return redirect('predictive')

    students = student.objects.filter(id__in=ids)

    predictresult = [{
        "STD_ID": s.id,
        "gender": s.gender,
        "name": s.name,
        "class_student": s.class_student,
        "result": get_prediction(s)
    } for s in students]

    return render(request, 'result.html', {'predictresult': predictresult})


@login_required(login_url='login_backend')
def cluster(request):
    return render(request, 'cluster.html')


@login_required(login_url='login_backend')
def student_list_cluster(request):
    if request.method != "POST":
        return redirect('cluster')

    class_std = request.POST.get('class_student')
    if not class_std:
        messages.error(request, "กรุณาป้อนข้อมูลให้ครบ")
        return redirect('cluster')

    sd = student.objects.filter(class_student=class_std)
    return render(request, 'cluster.html', {'sd': sd})


@login_required(login_url='login_backend')
def result_cluster(request):
    if request.method != "POST":
        return redirect('cluster')

    ids = request.POST.getlist('checkbox[]')
    if not ids:
        messages.error(request, "กรุณาเลือกนักเรียนอย่างน้อย 1 คน")
        return redirect('cluster')

    students = student.objects.filter(id__in=ids)

    predictresult_cluster = [{
        "STD_ID": s.id,
        "gender": s.gender,
        "name": s.name,
        "class_student": s.class_student,
        "result_cluster": get_cluster(s)
    } for s in students]

    return render(request, 'result_cluster.html', {
        'predictresult_cluster': predictresult_cluster
    })


def adduser_backend(request):
    if request.method != "POST":
        return redirect('register_backend')

    data = request.POST

    username = (data.get('username') or '').strip()
    email = (data.get('email') or '').strip()
    password = data.get('password')
    repassword = data.get('repassword')

    if not all([username, email, password, repassword]):
        messages.error(request, "กรุณาป้อนข้อมูลให้ครบ")
        return redirect('register_backend')

    if password != repassword:
        messages.error(request, "รหัสผ่านไม่ตรงกัน")
        return redirect('register_backend')

    if User.objects.filter(username=username).exists():
        messages.error(request, "Username นี้มีคนใช้แล้ว")
        return redirect('register_backend')

    if User.objects.filter(email=email).exists():
        messages.error(request, "อีเมลนี้เคยลงทะเบียนแล้ว")
        return redirect('register_backend')

    try:
        User.objects.create_user(
            first_name=data.get('first_name', ''),
            last_name=data.get('last_name', ''),
            username=username,
            email=email,
            password=password
        )
    except Exception:
        messages.error(request, "ไม่สามารถสร้างบัญชีได้ กรุณาลองใหม่")
        return redirect('register_backend')

    messages.success(request, "สร้างบัญชีเรียบร้อย")
    return redirect('login_backend')


def sign_in(request):
    if request.method != "POST":
        return redirect('login_backend')

    username = request.POST.get('username')
    password = request.POST.get('password')

    if not username or not password:
        messages.error(request, "กรุณาป้อนข้อมูลให้ครบ")
        return redirect('login_backend')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('home_backend')

    messages.error(request, "ไม่พบข้อมูลบัญชีผู้ใช้ หรือรหัสผ่านไม่ถูกต้อง")
    return redirect('login_backend')