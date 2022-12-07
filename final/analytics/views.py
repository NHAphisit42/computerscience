from django.shortcuts import redirect, render
from student.models import student, School, Eduction, Plan, Round_apply
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn import preprocessing
import matplotlib.pyplot as plt
from joblib import load
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.preprocessing import LabelEncoder

model_DT = load('./analytics/ML/DT.joblib')
model_RF = load('./analytics/ML/RF.joblib')
model_LR = load('./analytics/ML/LR.joblib')

# Create your views here.
# @login_required(login_url='login')
def home_backend(request):
    std = student.objects.all()
    stdcount = std.count()
    return render(request, 'home_backend.html', {'std':std, 'stdcount':stdcount})

def table_backend(request):
    std = student.objects.all()
    return render(request, 'student_table_backend.html', {'std':std})

def studentdetail(request,id):
    std = student.objects.get(id=id)
    return render(request, 'studentdetail.html', {'std':std})

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

def student_list(request):
    if request.method == "POST":
        class_std = request.POST['class_student']
        if class_std == "":
            messages.info(request,"กรุณาป้อนข้อมูลให้ครบ")
            redirect('predictive')
        else:
            print(class_std)
            std = student.objects.filter(class_student=class_std)
            return render(request, 'predictive.html', {'std':std})

# custom method for generating predictions
def getpredict(model_DT):
    predictions = model_DT.predict()
    if predictions == 1:
        return "ผ่าน"
    elif predictions == 0:
        return "ไม่ผ่าน"
    else:
        return "ผิดพลาด"
    
def result(request):
    if request.method == "POST":
        print("-----------------")
        print(request.POST)
        # Group_size = request.POST['Group_size']
        # plan = request.POST['plan']
        # round_apply = request.POST['round_apply']
        GPA = request.POST.getlist('GPA')
        grade_maths = request.POST.getlist('grade_maths')
        plan = request.POST.getlist('plan')
        print("-----------------")
        print(GPA)
        new_data = [(float(x1),float(x2),float(x3)) for x1,x2,x3 in zip(GPA,grade_maths,plan)]
        print(new_data)
            
        # write_program = request.POST['write_program']
        # trainprogram = request.POST['trainprogram']
        # family_income_per_month = request.POST['family_income_per_month']
        # status_family = request.POST['status_family']
        
        
        # dataset = 2.54
       
        # สร้างตัวแปรเก็บค่าที่ได้จากการทำนาย
        # y_pred_DT = model_DT.predict([dataset])
        # y_pred_RF = model_RF.predict([dataset])
        # y_pred_LR = model_LR.predict([dataset])

        
    return render(request, 'result.html')

def school(request):
    school = School.objects.all()
    return render(request, 'school.html', {'school':school})

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
            messages.info(request,"กรุณาป้อนข้อมูลให้ครบ")
            return redirect("addschool_backend")
        else:
            school = School.objects.create(
                name_school = name_school,
                size_school = size_school,
                zone_school = zone_school,
                district_school = district_school,
                province_school = province_school,
                Latitude = Latitude,
                Longitude = Longitude
            )
            school.save()
            messages.info(request,"สร้างสถานศึกษาเรียบร้อย")
            return redirect('addschool_backend')

def education(request):
    return render(request, 'education.html')

def plan(request):
    return render(request, 'plan.html')

def round_apply(request):
    return render(request, 'round_apply.html')

def adduser_backend(request):#ลงทะเบียน
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if username == "" or email == "" or password=="" or repassword=="":
            messages.info(request,"กรุณาป้อนข้อมูลให้ครบ")
            return redirect("register_backend")
        else:
            if password == repassword :
                if User.objects.filter(username=username).exists():
                    messages.info(request,"Username นี้มีคนใช้แล้ว")
                    return redirect("register_backend")
                elif User.objects.filter(email=email).exists():
                    messages.info(request,"อีเมลนี้เคยลงทะเบียนไปแล้ว")
                    return redirect("register_backend")
                else:
                    user = User.objects.create_user(
                        first_name = first_name,
                        last_name = last_name,
                        username = username,
                        email=email,
                        password=password
                    )
                    user.save()
                    messages.info(request,"สร้างบัญชีเรียบร้อย")
                    return redirect("login_backend")
            else:
                messages.info(request,"ไม่สามารถลงทะเบียนได้รหัสผ่านไม่ตรงกัน")
                return redirect("register_backend")

def sign_in(request):#ลงชื่อเข้าใช้
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_backend')
        else:
            messages.info(request,"ไม่พบข้อมูลบัญชีผู้ใช้")
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
        gender = request.POST['gender']
        name = request.POST['name']
        class_student = request.POST['sophomore_student']
        school = request.POST['school']
        short = request.POST['short']
        plan = request.POST['plan']
        round_apply = request.POST['round_apply']
        GPA = request.POST['grade']
        grade_maths = request.POST['grade_maths']
        grade_science = request.POST['grade_science']
        grade_english = request.POST['grade_english']
        skillcomputer = request.POST['ComputerSkillsCompetition']
        traincomputer = request.POST['ComputerRelatedtraining']
        write_program = request.POST['learnProgramming']
        trainprogram = request.POST['programmingTraining']
        Other_skills = request.POST['Other_skills']
        want_to_develop = request.POST['improve_skills']
        family_income_per_month = request.POST['family_income_per_month']
        status_family = request.POST['family_status']
        which_channel_do_you_know = request.POST['Known_from_any_channel']
        why_did_you_choose_to_study = request.POST['why_did_you_choose_to_study']
        ex1 = request.POST['ex1']
        ex2 = request.POST['ex2']
        ex3 = request.POST['ex3']
        ex4 = request.POST['ex4']
        ex5 = request.POST['ex5']
        ex6 = request.POST['ex6']
        ex7 = request.POST['ex7']
        ex8 = request.POST['ex8']
        ex9 = request.POST['ex9']
        ex10 = request.POST['ex10']
        ex11 = request.POST['ex11']
        ex12 = request.POST['ex12']
        ex13 = request.POST['ex13']
        ex14 = request.POST['ex14']
        ex15 = request.POST['ex15']
        ex16 = request.POST['ex16']
        ex17 = request.POST['ex17']
        ex18 = request.POST['ex18']
        ex19 = request.POST['ex19']
        ex20 = request.POST['ex20']

        std = student.objects.create(
            gender = gender,
            name = name,
            class_student = class_student,
            school = school,
            short = short,
            plan = plan,
            round_apply = round_apply,
            GPA = GPA,
            grade_maths = grade_maths,
            grade_science = grade_science,
            grade_english = grade_english,
            skillcomputer = skillcomputer,
            traincomputer = traincomputer,
            write_program = write_program,
            trainprogram = trainprogram,
            Other_skills = Other_skills,
            want_to_develop = want_to_develop,
            family_income_per_month = family_income_per_month,
            status_family = status_family,
            which_channel_do_you_know = which_channel_do_you_know,
            why_did_you_choose_to_study = why_did_you_choose_to_study,
            ex1 = ex1,
            ex2 = ex2,
            ex3 = ex3,
            ex4 = ex4,
            ex5 = ex5,
            ex6 = ex6,
            ex7 = ex7,
            ex8 = ex8,
            ex9 = ex9,
            ex10 = ex10,
            ex11 = ex11,
            ex12 = ex12,
            ex13 = ex13,
            ex14 = ex14,
            ex15 = ex15,
            ex16 = ex16,
            ex17 = ex17,
            ex18 = ex18,
            ex19 = ex19,
            ex20 = ex20,
        )
        std.save()
        return redirect('table_backend')