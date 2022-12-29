from distutils.log import info
from django.shortcuts import redirect, render
from student.models import student
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')

def form(request):
    return render(request, 'form.html')

def addstudent(request):
    if request.method == "POST":
        gender = request.POST['gender']
        name = request.POST['name']
        class_student = request.POST['class_student']
        school = request.POST['school']
        short = request.POST['short']
        school_size = request.POST['school_size']
        plan = request.POST['plan']
        round_apply = request.POST['round_apply']
        GPA = request.POST['GPA']
        grade_maths = request.POST['grade_maths']
        grade_science = request.POST['grade_science']
        grade_english = request.POST['grade_english']
        skillcomputer = request.POST['skillcomputer']
        traincomputer = request.POST['traincomputer']
        write_program = request.POST['write_program']
        trainprogram = request.POST['trainprogram']
        Other_skills = request.POST['Other_skills']
        want_to_develop = request.POST['want_to_develop']
        family_income_per_month = request.POST['family_income_per_month']
        status_family = request.POST['status_family']
        which_channel_do_you_know = request.POST['which_channel_do_you_know']
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

        if gender == "" and name == "":
            messages.info(request, "กรุณากรอกข้อมูลให้ครบ")
        else:
            std = student.objects.create(
                gender = gender,
                name = name,
                class_student = class_student,
                school = school,
                short = short,
                school_size = school_size,
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
            messages.info(request, "กรอกข้อมูลครบถ้วน")
            return redirect('formstudent')