from django.shortcuts import redirect, render
from student.models import student, Eduction, Round_apply, Plan, School

# Create your views here.
def home(request):
    return render(request, 'home.html')

def form(request):
    school = School.objects.all()
    education = Eduction.objects.all()
    round = Round_apply.objects.all()
    plan = Plan.objects.all()
    return render(request, 'form.html', {'school': school, 'education': education, 'round': round, 'plan': plan})

def addstudent(request):
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

        if gender == "":
            pass
        else:
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
            return redirect('home')