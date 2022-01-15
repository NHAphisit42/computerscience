from django.db import models

# Create your models here.

class student(models.Model):
    gender_CHOICE = (('นาย', 'นาย'), ('นางสาว', 'นางสาว'), ('นาง', 'นาง'),)

    grade_CHOICE = (('ชั้นปีที่ 1', 'ชั้นปีที่ 1'), ('ชั้นปีที่ 2', 'ชั้นปีที่ 2'), ('ชั้นปีที่ 3', 'ชั้นปีที่ 3'), ('ชั้นปีที่ 4', 'ชั้นปีที่ 4'),)

    plan_CHOICE = (
        ('แผนกการเรียน วิทย์-คณิต', 'แผนกการเรียน วิทย์-คณิต'), 
        ('แผนกการเรียน ศิลป์-คำนวณ','แผนกการเรียน ศิลป์-คำนวณ'),
        ('แผนกการเรียน ศิลป์-ภาษา','แผนกการเรียน ศิลป์-ภาษา'),
        ('แผนกการเรียน คณิตศาสตร์-ภาษาอังกฤษ','แผนกการเรียน คณิตศาสตร์-ภาษาอังกฤษ'), 
        ('แผนกการเรียน ภาษา-สังคม','แผนกการเรียน ภาษา-สังคม'),
        ('แผนกการเรียน สังคม-ญี่ปุ่น','แผนกการเรียน ภาษา-ญี่ปุ่น'),
        ('ประกาศนียบัตรวิชาชีพ(ปวช)','ประกาศนียบัตรวิชาชีพ(ปวช)'), 
        ('ประกาศนียบัตรวิชาชีพขั้นสูง(ปวส)','ประกาศนียบัตรวิชาชีพขั้นสูง(ปวส)'),
        ('เทียบเท่าละดับมัธยมศึกษาตอนปลาย)','เทียบเท่าละดับมัธยมศึกษาตอนปลาย'),
        )

    aroundregister_CHOICE = (
        ('portfolio', 'portfolio'),
        ('โควต้า', 'โควต้า'),
        ('รับตรงรอบที่ 1 ', 'รับตรงรอบที่ 1 '),
        ('รับตรงรอบที่ 2 ', 'รับตรงรอบที่ 2 '),
        ('รับตรง(เพิ่มเติม)', 'รับตรง(เพิ่มเติม)'),
    )

    ComputerSkillsCompetition_CHOICE = (
        ('เคย', 'เคย'),
        ('ไม่เคย', 'ไม่เคย'),
    )

    ComputerRelatedtraining_CHOICE = (
        ('เคย', 'เคย'),
        ('ไม่เคย', 'ไม่เคย'),
    )

    learnProgramming_CHOICE = (
        ('เคย', 'เคย'),
        ('ไม่เคย', 'ไม่เคย'),
    )
    
    programmingTraining_CHOICE = (
        ('เคย', 'เคย'),
        ('ไม่เคย', 'ไม่เคย'),
    )

    family_income_per_month_CHOICE = (
        ('ไม่เกิน 5,000 บาท', 'ไม่เกิน 5,000 บาท'),
        ('5,001 ถึง 10,000 บาท', '5,001 ถึง 10,000 บาท'),
        ('10,001 ถึง 15,000 บาท', '10,001 ถึง 15,000 บาท'),
        ('15,001 ถึง 20,000 บาท', '15,001 ถึง 20,000 บาท'),
        ('25,001 บาทขึ้นไป', '25,001 บาทขึ้นไป'),
    )

    family_status_CHOICE = (
        ('บิดา มารดาอยู่ด้วยกัน', 'บิดา มารดาอยู่ด้วยกัน'),
        ('บิดา มารดาหย่าร้างกัน', 'บิดา มารดาหย่าร้างกัน'),
        ('บิดาถึงแก่กรรม', 'บิดาถึงแก่กรรม'),
        ('มารดาถึงแก่กรรม', 'มารดาถึงแก่กรรม'),
        ('อยู่กับบิดา', 'อยู่กับบิดา'),
        ('อยู่กับมารดา', 'อยู่กับมารดา'),
    )

    ex1_CHOICE = (('0', 'เห็นด้วยอย่างยิ่ง'), ('1', 'เห็นด้วย'), ('2', 'ไม่เห็นด้วย'), ('3','ไม่เห็นด้วยอย่างยิ่ง'),)

    ex2_CHOICE = (('3', 'เห็นด้วยอย่างยิ่ง'), ('2', 'เห็นด้วย'), ('1', 'ไม่เห็นด้วย'), ('0','ไม่เห็นด้วยอย่างยิ่ง'),)

    ex3_CHOICE = (('3', 'เห็นด้วยอย่างยิ่ง'), ('2', 'เห็นด้วย'), ('1', 'ไม่เห็นด้วย'), ('0','ไม่เห็นด้วยอย่างยิ่ง'),)

    ex4_CHOICE = (('0', 'เห็นด้วยอย่างยิ่ง'), ('1', 'เห็นด้วย'), ('2', 'ไม่เห็นด้วย'), ('3','ไม่เห็นด้วยอย่างยิ่ง'),)

    ex5_CHOICE = (('3', 'เห็นด้วยอย่างยิ่ง'), ('2', 'เห็นด้วย'), ('1', 'ไม่เห็นด้วย'), ('0','ไม่เห็นด้วยอย่างยิ่ง'),)

    ex6_CHOICE = (('3', 'เห็นด้วยอย่างยิ่ง'), ('2', 'เห็นด้วย'), ('1', 'ไม่เห็นด้วย'), ('0','ไม่เห็นด้วยอย่างยิ่ง'),)

    ex7_CHOICE = (('0', 'เห็นด้วยอย่างยิ่ง'), ('1', 'เห็นด้วย'), ('2', 'ไม่เห็นด้วย'), ('3','ไม่เห็นด้วยอย่างยิ่ง'),)

    ex8_CHOICE = (('0', 'เห็นด้วยอย่างยิ่ง'), ('1', 'เห็นด้วย'), ('2', 'ไม่เห็นด้วย'), ('3','ไม่เห็นด้วยอย่างยิ่ง'),)

    ex9_CHOICE = (('3', 'เห็นด้วยอย่างยิ่ง'), ('2', 'เห็นด้วย'), ('1', 'ไม่เห็นด้วย'), ('0','ไม่เห็นด้วยอย่างยิ่ง'),)

    ex10_CHOICE = (('3', 'เห็นด้วยอย่างยิ่ง'), ('2', 'เห็นด้วย'), ('1', 'ไม่เห็นด้วย'), ('0','ไม่เห็นด้วยอย่างยิ่ง'),)

    ex11_CHOICE = (('0', 'เห็นด้วยอย่างยิ่ง'), ('1', 'เห็นด้วย'), ('2', 'ไม่เห็นด้วย'), ('3','ไม่เห็นด้วยอย่างยิ่ง'),)

    ex12_CHOICE = (('0', 'เห็นด้วยอย่างยิ่ง'), ('1', 'เห็นด้วย'), ('2', 'ไม่เห็นด้วย'), ('3','ไม่เห็นด้วยอย่างยิ่ง'),)

    ex13_CHOICE = (('3', 'เห็นด้วยอย่างยิ่ง'), ('2', 'เห็นด้วย'), ('1', 'ไม่เห็นด้วย'), ('0','ไม่เห็นด้วยอย่างยิ่ง'),)

    ex14_CHOICE = (('0', 'เห็นด้วยอย่างยิ่ง'), ('1', 'เห็นด้วย'), ('2', 'ไม่เห็นด้วย'), ('3','ไม่เห็นด้วยอย่างยิ่ง'),)

    ex15_CHOICE = (('3', 'เห็นด้วยอย่างยิ่ง'), ('2', 'เห็นด้วย'), ('1', 'ไม่เห็นด้วย'), ('0','ไม่เห็นด้วยอย่างยิ่ง'),)

    ex16_CHOICE = (('0', 'เห็นด้วยอย่างยิ่ง'), ('1', 'เห็นด้วย'), ('2', 'ไม่เห็นด้วย'), ('3','ไม่เห็นด้วยอย่างยิ่ง'),)

    ex17_CHOICE = (('0', 'เห็นด้วยอย่างยิ่ง'), ('1', 'เห็นด้วย'), ('2', 'ไม่เห็นด้วย'), ('3','ไม่เห็นด้วยอย่างยิ่ง'),)

    ex18_CHOICE = (('3', 'เห็นด้วยอย่างยิ่ง'), ('2', 'เห็นด้วย'), ('1', 'ไม่เห็นด้วย'), ('0','ไม่เห็นด้วยอย่างยิ่ง'),)

    ex19_CHOICE = (('3', 'เห็นด้วยอย่างยิ่ง'), ('2', 'เห็นด้วย'), ('1', 'ไม่เห็นด้วย'), ('0','ไม่เห็นด้วยอย่างยิ่ง'),)

    ex20_CHOICE = (('0', 'เห็นด้วยอย่างยิ่ง'), ('1', 'เห็นด้วย'), ('2', 'ไม่เห็นด้วย'), ('3','ไม่เห็นด้วยอย่างยิ่ง'),)


    gender = models.CharField(max_length=100, choices=gender_CHOICE, null=True)
    name = models.CharField(max_length=255, null=True)
    sophomore_student = models.CharField(max_length=155, choices=grade_CHOICE, null=True)
    school = models.CharField(max_length=255, null=True)
    short = models.CharField(max_length=100, null=True)
    plan = models.CharField(max_length=255, choices=plan_CHOICE, null=True)
    round_apply = models.CharField(max_length=255, choices=aroundregister_CHOICE, null=True)
    grade = models.CharField(max_length=50, null=True)
    grade_maths = models.CharField(max_length=50, null=True)
    grade_science = models.CharField(max_length=50, null=True)
    grade_english = models.CharField(max_length=50, null=True)
    ComputerSkillsCompetition = models.CharField(max_length=255, choices=ComputerSkillsCompetition_CHOICE, null=True)
    ComputerRelatedtraining = models.CharField(max_length=255, choices=ComputerRelatedtraining_CHOICE, null=True)
    learnProgramming = models.CharField(max_length=255, choices=learnProgramming_CHOICE, null=True)
    programmingTraining =models.CharField(max_length=255, choices=programmingTraining_CHOICE, null=True)
    Other_skills = models.TextField(null=True)
    improve_skills = models.TextField(null=True)
    family_income_per_month = models.CharField(max_length=255, choices=family_income_per_month_CHOICE, null=True)
    family_status = models.CharField(max_length=255, choices=family_status_CHOICE, null=True)
    Known_from_any_channel = models.TextField(null=True)
    why_did_you_choose_to_study = models.TextField(null=True)
    ex1 = models.IntegerField(choices=ex1_CHOICE)
    ex2 = models.IntegerField(choices=ex2_CHOICE)
    ex3 = models.IntegerField(choices=ex3_CHOICE)
    ex4 = models.IntegerField(choices=ex4_CHOICE)
    ex5 = models.IntegerField(choices=ex5_CHOICE)
    ex6 = models.IntegerField(choices=ex6_CHOICE)
    ex7 = models.IntegerField(choices=ex7_CHOICE)
    ex8 = models.IntegerField(choices=ex8_CHOICE)
    ex9 = models.IntegerField(choices=ex9_CHOICE)
    ex10 = models.IntegerField(choices=ex10_CHOICE)
    ex11 = models.IntegerField(choices=ex11_CHOICE)
    ex12 = models.IntegerField(choices=ex12_CHOICE)
    ex13 = models.IntegerField(choices=ex13_CHOICE)
    ex14 = models.IntegerField(choices=ex14_CHOICE)
    ex15 = models.IntegerField(choices=ex15_CHOICE)
    ex16 = models.IntegerField(choices=ex16_CHOICE)
    ex17 = models.IntegerField(choices=ex17_CHOICE)
    ex18 = models.IntegerField(choices=ex18_CHOICE)
    ex19 = models.IntegerField(choices=ex19_CHOICE)
    ex20 = models.IntegerField(choices=ex20_CHOICE)

    def __str__(self):
        return self.name