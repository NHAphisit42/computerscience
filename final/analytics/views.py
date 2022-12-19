from django.shortcuts import redirect, render
from student.models import student, School, Eduction, Plan, Round_apply
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from joblib import load
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import json
from sklearn.preprocessing import LabelEncoder
from student.models import student
import array

student.plan_no
student.status_family_no
student.write_program_no
student.trainprogram_no
student.round_apply_no
student.school_size_no
student.family_income_per_month_no

model_DT = load('./analytics/ML/DCT.joblib')
# model_DT = load('./analytics/ML/DCT.joblib')
# model_RF = load('./analytics/ML/RF.joblib')
# model_LR = load('./analytics/ML/LR.joblib')

# Create your views here.
# @login_required(login_url='login')
def home_backend(request):
    std = student.objects.all()
    return render(request, 'home_backend.html', {'std': std})


def table_backend(request):
    std = student.objects.all()
    count = std.count()
    return render(request, 'student_table_backend.html', {'std': std, 'count': count})


def studentdetail(request, id):
    std = student.objects.get(id=id)
    return render(request, 'studentdetail.html', {'std': std})


def chart_backend(request):
    return render(request, 'chart_backend.html')


def addschool_backend(request):
    return render(request, 'addschool_backend.html')


def login_backend(request):
    return render(request, 'login_backend.html')


def register_backend(request):
    return render(request, 'register_backend.html')


def predictive(request):
    return render(request, 'predictive.html')


std_select = []
def student_list(request):
    if request.method == "POST":
        class_std = request.POST['class_student']
        if class_std == "":
            messages.info(request, "กรุณาป้อนข้อมูลให้ครบ")
            redirect('predictive')
        else:
            print(class_std)
            sd = student.objects.filter(class_student=class_std)
            global std_select 
            std_select = sd
            return render(request, 'predictive.html', {'sd': sd})
        

def result(request):
    data = []
    if request.method == "POST":
        checkbox = request.POST.getlist('checkbox[]')
        if len(checkbox) > 0:
            for i in range(len(checkbox)):
                for y in range(len(std_select)):
                    if int(std_select[y].id) == int(checkbox[i]):
                        data.append({
                            "STD_ID" : checkbox[i],
                            "name" : std_select[y].name,
                            "class_student" : std_select[y].class_student,
                            "GPA" : std_select[y].GPA,
                            "write_program" : student.write_program_no(std_select[y]),
                            "trainprogram" :student.trainprogram_no(std_select[y]),
                            "plan" : student.plan_no(std_select[y]),
                            "status_family" : student.status_family_no(std_select[y]),
                            "round_apply" : student.round_apply_no(std_select[y]),
                            "school_size" : student.school_size_no(std_select[y]),
                            "family_income_per_month" : student.family_income_per_month_no(std_select[y]),
                        })
            print(data)
            for n in data:
                result = getPredictions(n['GPA'], 
                                        n['write_program'], 
                                        n['trainprogram'], 
                                        n['plan'], 
                                        n['status_family'], 
                                        n['round_apply'], 
                                        n['school_size'], 
                                        n['family_income_per_month'])      
                return render(request, 'result.html', {'data': data, 'result': result})


def getPredictions(school_size, plan, round_apply, GPA, write_program, trainprogram, family_income_per_month, status_family):
    predictions = model_DT.predict([[school_size, plan, round_apply, GPA, write_program, trainprogram, family_income_per_month, status_family]])
    if predictions == 1:
        return "PASS"
    elif predictions == 0:
        return "NOT PASS"
    else:
        return "ERROR"


def school(request):
    school = School.objects.all()
    return render(request, 'school.html', {'school': school})


def addschool(request):
    if request.method == "POST":
        name_school = request.POST['name_school']
        size_school = request.POST['size_school']
        zone_school = request.POST['zone_school']
        district_school = request.POST['district_school']
        province_school = request.POST['province_school']
        Latitude = request.POST['Latitude']
        Longitude = request.POST['Longitude']

        if name_school == "" or size_school == "" or zone_school == "" or district_school == "" or province_school == "" or Latitude == "" or Longitude == "":
            messages.info(request, "กรุณาป้อนข้อมูลให้ครบ")
            return redirect("addschool_backend")
        else:
            school = School.objects.create(
                name_school=name_school,
                size_school=size_school,
                zone_school=zone_school,
                district_school=district_school,
                province_school=province_school,
                Latitude=Latitude,
                Longitude=Longitude
            )
            school.save()
            messages.info(request, "สร้างสถานศึกษาเรียบร้อย")
            return redirect('addschool_backend')


def education(request):
    return render(request, 'education.html')


def plan(request):
    return render(request, 'plan.html')


def round_apply(request):
    return render(request, 'round_apply.html')


def adduser_backend(request):  # ลงทะเบียน
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if username == "" or email == "" or password == "" or repassword == "":
            messages.info(request, "กรุณาป้อนข้อมูลให้ครบ")
            return redirect("register_backend")
        else:
            if password == repassword:
                if User.objects.filter(username=username).exists():
                    messages.info(request, "Username นี้มีคนใช้แล้ว")
                    return redirect("register_backend")
                elif User.objects.filter(email=email).exists():
                    messages.info(request, "อีเมลนี้เคยลงทะเบียนไปแล้ว")
                    return redirect("register_backend")
                else:
                    user = User.objects.create_user(
                        first_name=first_name,
                        last_name=last_name,
                        username=username,
                        email=email,
                        password=password
                    )
                    user.save()
                    messages.info(request, "สร้างบัญชีเรียบร้อย")
                    return redirect("login_backend")
            else:
                messages.info(
                    request, "ไม่สามารถลงทะเบียนได้รหัสผ่านไม่ตรงกัน")
                return redirect("register_backend")


def sign_in(request):  # ลงชื่อเข้าใช้
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_backend')
        else:
            messages.info(request, "ไม่พบข้อมูลบัญชีผู้ใช้")
            return redirect("login_backend")


def logout_backend(request):
    logout(request)
    return redirect('home_backend')


def remove(request, id):
    std = student.objects.get(id=id)
    std.delete()
    return redirect('table_backend')


def update(request, id):
    std = student.objects.get(id=id)
    if request.method == "POST":
        std.gender = request.POST.get('gender')
        std.name = request.POST.get('name')
        std.class_student = request.POST.get('sophomore_student')
        std.school = request.POST.get('school')
        std.short = request.POST.get('short')
        std.plan = request.POST.get('plan')
        std.round_apply = request.POST.get('round_apply')
        std.GPA = request.POST.get('grade')
        std.grade_maths = request.POST.get('grade_maths')
        std.grade_science = request.POST.get('grade_science')
        std.grade_english = request.POST.get('grade_english')
        std.skillcomputer = request.POST.get('ComputerSkillsCompetition')
        std.traincomputer = request.POST.get('ComputerRelatedtraining')
        std.write_program = request.POST.get('learnProgramming')
        std.trainprogram = request.POST.get('programmingTraining')
        std.Other_skills = request.POST.get('Other_skills')
        std.want_to_develop = request.POST.get('improve_skills')
        std.family_income_per_month = request.POST.get('family_income_per_month')
        std.status_family = request.POST.get('family_status')
        std.which_channel_do_you_know = request.POST.get('Known_from_any_channel')
        std.why_did_you_choose_to_study = request.POST.get('why_did_you_choose_to_study')
        std.ex1 = request.POST.get('ex1')
        std.ex2 = request.POST.get('ex2')
        std.ex3 = request.POST.get('ex3')
        std.ex4 = request.POST.get('ex4')
        std.ex5 = request.POST.get('ex5')
        std.ex6 = request.POST.get('ex6')
        std.ex7 = request.POST.get('ex7')
        std.ex8 = request.POST.get('ex8')
        std.ex9 = request.POST.get('ex9')
        std.ex10 = request.POST.get('ex10')
        std.ex11 = request.POST.get('ex11')
        std.ex12 = request.POST.get('ex12')
        std.ex13 = request.POST.get('ex13')
        std.ex14 = request.POST.get('ex14')
        std.ex15 = request.POST.get('ex15')
        std.ex16 = request.POST.get('ex16')
        std.ex17 = request.POST.get('ex17')
        std.ex18 = request.POST.get('ex18')
        std.ex19 = request.POST.get('ex19')
        std.ex20 = request.POST.get('ex20')
        std.save()
        redirect('table_backend')
