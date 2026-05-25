from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from joblib import load

from student.models import student

# =========================
# ML Models
# =========================
model_logistic = load('./analytics/ML/Logistics.joblib')
model_cluster = load('./analytics/ML/clustering.joblib')

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
        float(std.GPA),
        student.write_program_no(std),
        student.trainprogram_no(std),
        student.family_income_per_month_no(std),
        student.status_family_no(std)
    ]]

    result = model_logistic.predict(data)[0]
    return "ผ่าน" if result else "ไม่ผ่าน"


def get_cluster(std):
    data = [[
        float(std.GPA),
        student.plan_no(std),
        student.write_program_no(std)
    ]]

    result = model_cluster.predict(data)[0]

    cluster_text = {
        0: "เน้นปูพื้นฐานเขียนโปรแกรมและภาษา",
        1: "ทบทวนพื้นฐานเขียนโปรแกรมและคำนวณ",
        2: "ปูพื้นฐานเขียนโปรแกรมและคำนวณ"
    }

    return cluster_text.get(result, "ไม่พบข้อมูล")


# =========================
# Views
# =========================
@login_required(login_url='login_backend')
def home_backend(request):
    std = student.objects.only('id', 'name', 'class_student')
    return render(request, 'home_backend.html', {'std': std})


def table_backend(request):
    std = student.objects.all()
    return render(request, 'student_table_backend.html', {
        'std': std,
        'count': std.count()
    })


def remove(request, id):
    get_object_or_404(student, id=id).delete()
    messages.success(request, "ลบข้อมูลเรียบร้อยแล้ว")
    return redirect('table_backend')


def studentdetail(request, id):
    std = get_object_or_404(student, id=id)

    if request.method == "POST":

        for field in STUDENT_FIELDS:
            setattr(std, field, request.POST.get(field))

        std.save()

        messages.success(request, "แก้ไขข้อมูลเรียบร้อยแล้ว")
        return redirect('table_backend')

    total = sum(getattr(std, f, 0) for f in EX_FIELDS)

    return render(request, 'studentdetail.html', {
        'std': std,
        'sum': get_growthmindset(total)
    })


def login_backend(request):
    return render(request, 'login_backend.html')


def logout_backend(request):
    logout(request)
    return redirect('home_backend')


def register_backend(request):
    return render(request, 'register_backend.html')


def predictive(request):
    return render(request, 'predictive.html')


def student_list(request):
    class_std = request.POST.get('class_student')

    if not class_std:
        messages.error(request, "กรุณาป้อนข้อมูลให้ครบ")
        return redirect('predictive')

    sd = student.objects.filter(class_student=class_std)

    return render(request, 'predictive.html', {'sd': sd})


def result(request):

    ids = request.POST.getlist('checkbox[]')

    students = student.objects.filter(id__in=ids)

    predictresult = [{
        "STD_ID": s.id,
        "gender": s.gender,
        "name": s.name,
        "class_student": s.class_student,
        "result": get_prediction(s)
    } for s in students]

    return render(request, 'result.html', {
        'predictresult': predictresult
    })


def cluster(request):
    return render(request, 'cluster.html')


def student_list_cluster(request):
    class_std = request.POST.get('class_student')

    if not class_std:
        messages.error(request, "กรุณาป้อนข้อมูลให้ครบ")
        return redirect('cluster')

    sd = student.objects.filter(class_student=class_std)

    return render(request, 'cluster.html', {'sd': sd})


def result_cluster(request):

    ids = request.POST.getlist('checkbox[]')

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

    username = data.get('username')
    email = data.get('email')
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

    User.objects.create_user(
        first_name=data.get('first_name'),
        last_name=data.get('last_name'),
        username=username,
        email=email,
        password=password
    )

    messages.success(request, "สร้างบัญชีเรียบร้อย")
    return redirect('login_backend')


def sign_in(request):

    if request.method != "POST":
        return redirect('login_backend')

    user = authenticate(
        request,
        username=request.POST.get('username'),
        password=request.POST.get('password')
    )

    if user:
        login(request, user)
        return redirect('home_backend')

    messages.error(request, "ไม่พบข้อมูลบัญชีผู้ใช้")
    return redirect('login_backend')