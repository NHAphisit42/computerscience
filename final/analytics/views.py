from django.shortcuts import redirect, render
from student.models import student
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url='login_backend.html')
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

def school(request):
    return render(request, 'school.html')

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
                    user=User.objects.create_user(
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
        sophomore_student = request.POST['sophomore_student']
        school = request.POST['school']
        short = request.POST['short']
        plan = request.POST['plan']
        round_apply = request.POST['round_apply']
        grade = request.POST['grade']
        grade_maths = request.POST['grade_maths']
        grade_science = request.POST['grade_science']
        grade_english = request.POST['grade_english']
        ComputerSkillsCompetition = request.POST['ComputerSkillsCompetition']
        ComputerRelatedtraining = request.POST['ComputerRelatedtraining']
        learnProgramming = request.POST['learnProgramming']
        programmingTraining = request.POST['programmingTraining']
        Other_skills = request.POST['Other_skills']
        improve_skills = request.POST['improve_skills']
        family_income_per_month = request.POST['family_income_per_month']
        family_status = request.POST['family_status']
        Known_from_any_channel = request.POST['Known_from_any_channel']
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
            sophomore_student = sophomore_student,
            school = school,
            short = short,
            plan = plan,
            round_apply = round_apply,
            grade = grade,
            grade_maths = grade_maths,
            grade_science = grade_science,
            grade_english = grade_english,
            ComputerSkillsCompetition = ComputerSkillsCompetition,
            ComputerRelatedtraining = ComputerRelatedtraining,
            learnProgramming = learnProgramming,
            programmingTraining = programmingTraining,
            Other_skills = Other_skills,
            improve_skills = improve_skills,
            family_income_per_month = family_income_per_month,
            family_status = family_status,
            Known_from_any_channel = Known_from_any_channel,
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

