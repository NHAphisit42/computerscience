from unicodedata import name
from django.db import models

# Create your models here.

class School(models.Model):
    SizeSchool_CHOICE = (
        ('โรงเรียนขนาดเล็ก', 'โรงเรียนขนาดเล็ก'), 
        ('โรงเรียนขนาดกลาง', 'โรงเรียนขนาดกลาง'), 
        ('โรงเรียนขนาดใหญ่', 'โรงเรียนขนาดใหญ่'), 
        ('โรงเรียนขนาดใหญ่พิเศษ', 'โรงเรียนขนาดใหญ่พิเศษ'),)

    name_school = models.CharField(max_length=255)
    size_school = models.CharField(max_length=255, choices=SizeSchool_CHOICE)
    zone_school = models.CharField(max_length=255)
    district_school = models.CharField(max_length=255)
    province_school = models.CharField(max_length=255)
    Latitude = models.CharField(max_length=255)
    Longitude = models.CharField(max_length=255)

    def __str__(self):
        return self.name_school

    class Meta:
        db_table='School'
        verbose_name='โรงเรียน'
        verbose_name_plural="ข้อมูลโรงเรียน"

class Eduction(models.Model):
    education_name = models.CharField(max_length=255)

    def __str__(self):
        return self.education_name

    class Meta:
        db_table='Eduction'
        verbose_name='การศึกษา'
        verbose_name_plural="ข้อมูลการศึกษา"

class Round_apply(models.Model):
    round_apply_name = models.CharField(max_length=255)

    def __str__(self):
        return self.round_apply_name

    class Meta:
        db_table='Round_apply'
        verbose_name='รอบที่สมัคร'
        verbose_name_plural="ข้อมูลรอบบสมัคร"
        
class Plan(models.Model):
    plan_name = models.CharField(max_length=255)

    def __str__(self):
        return self.plan_name

    class Meta:
        db_table='Plan'
        verbose_name='แผนการเรียน'
        verbose_name_plural="ข้อมูลแผนการเรียน"

class student(models.Model):
    gender_CHOICE = (('นาย', 'นาย'), ('นางสาว', 'นางสาว'), ('นาง', 'นาง'),)

    class_student_CHOICE = (
        ('รุ่น61', 'รุ่น61'), ('รุ่น62', 'รุ่น62'), ('รุ่น63', 'รุ่น63'), ('รุ่น64', 'รุ่น64'),
        ('รุ่น65', 'รุ่น65'), ('รุ่น66', 'รุ่น66'), ('รุ่น67', 'รุ่น67'), ('รุ่น68', 'รุ่น68'),
        )
    
    school_size_CHOICE = (('โรงเรียนขนาดเล็ก', 'โรงเรียนขนาดเล็ก'), ('โรงเรียนขนาดกลาง', 'โรงเรียนขนาดกลาง'), ('โรงเรียนขนาดใหญ่', 'โรงเรียนขนาดใหญ่'))

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

    ex1_CHOICE = ((0, 'เห็นด้วยอย่างยิ่ง'), (1, 'เห็นด้วย'), (2, 'ไม่เห็นด้วย'), (3,'ไม่เห็นด้วยอย่างยิ่ง'),)

    ex2_CHOICE = ((3, 'เห็นด้วยอย่างยิ่ง'), (2, 'เห็นด้วย'), (1, 'ไม่เห็นด้วย'), (0,'ไม่เห็นด้วยอย่างยิ่ง'),)

    ex3_CHOICE = ((3, 'เห็นด้วยอย่างยิ่ง'), (2, 'เห็นด้วย'), (1, 'ไม่เห็นด้วย'), (0,'ไม่เห็นด้วยอย่างยิ่ง'),)

    ex4_CHOICE = ((0, 'เห็นด้วยอย่างยิ่ง'), (1, 'เห็นด้วย'), (2, 'ไม่เห็นด้วย'), (3,'ไม่เห็นด้วยอย่างยิ่ง'),)

    ex5_CHOICE = ((3, 'เห็นด้วยอย่างยิ่ง'), (2, 'เห็นด้วย'), (1, 'ไม่เห็นด้วย'), (0,'ไม่เห็นด้วยอย่างยิ่ง'),)

    ex6_CHOICE = ((3, 'เห็นด้วยอย่างยิ่ง'), (2, 'เห็นด้วย'), (1, 'ไม่เห็นด้วย'), (0,'ไม่เห็นด้วยอย่างยิ่ง'),)

    ex7_CHOICE = ((0, 'เห็นด้วยอย่างยิ่ง'), (1, 'เห็นด้วย'), (2, 'ไม่เห็นด้วย'), (3,'ไม่เห็นด้วยอย่างยิ่ง'),)

    ex8_CHOICE = ((0, 'เห็นด้วยอย่างยิ่ง'), (1, 'เห็นด้วย'), (2, 'ไม่เห็นด้วย'), (3,'ไม่เห็นด้วยอย่างยิ่ง'),)

    ex9_CHOICE = ((3, 'เห็นด้วยอย่างยิ่ง'), (2, 'เห็นด้วย'), (1, 'ไม่เห็นด้วย'), (0,'ไม่เห็นด้วยอย่างยิ่ง'),)

    ex10_CHOICE = ((3, 'เห็นด้วยอย่างยิ่ง'), (2, 'เห็นด้วย'), (1, 'ไม่เห็นด้วย'), (0,'ไม่เห็นด้วยอย่างยิ่ง'),)

    ex11_CHOICE = ((0, 'เห็นด้วยอย่างยิ่ง'), (1, 'เห็นด้วย'), (2, 'ไม่เห็นด้วย'), (3,'ไม่เห็นด้วยอย่างยิ่ง'),)

    ex12_CHOICE = ((0, 'เห็นด้วยอย่างยิ่ง'), (1, 'เห็นด้วย'), (2, 'ไม่เห็นด้วย'), (3,'ไม่เห็นด้วยอย่างยิ่ง'),)

    ex13_CHOICE = ((3, 'เห็นด้วยอย่างยิ่ง'), (2, 'เห็นด้วย'), (1, 'ไม่เห็นด้วย'), (0,'ไม่เห็นด้วยอย่างยิ่ง'),)

    ex14_CHOICE = ((0, 'เห็นด้วยอย่างยิ่ง'), (1, 'เห็นด้วย'), (2, 'ไม่เห็นด้วย'), (3,'ไม่เห็นด้วยอย่างยิ่ง'),)

    ex15_CHOICE = ((3, 'เห็นด้วยอย่างยิ่ง'), (2, 'เห็นด้วย'), (1, 'ไม่เห็นด้วย'), (0,'ไม่เห็นด้วยอย่างยิ่ง'),)

    ex16_CHOICE = ((0, 'เห็นด้วยอย่างยิ่ง'), (1, 'เห็นด้วย'), (2, 'ไม่เห็นด้วย'), (3,'ไม่เห็นด้วยอย่างยิ่ง'),)

    ex17_CHOICE = ((0, 'เห็นด้วยอย่างยิ่ง'), (1, 'เห็นด้วย'), (2, 'ไม่เห็นด้วย'), (3,'ไม่เห็นด้วยอย่างยิ่ง'),)

    ex18_CHOICE = ((3, 'เห็นด้วยอย่างยิ่ง'), (2, 'เห็นด้วย'), (1, 'ไม่เห็นด้วย'), (0,'ไม่เห็นด้วยอย่างยิ่ง'),)

    ex19_CHOICE = ((3, 'เห็นด้วยอย่างยิ่ง'), (2, 'เห็นด้วย'), (1, 'ไม่เห็นด้วย'), (0,'ไม่เห็นด้วยอย่างยิ่ง'),)

    ex20_CHOICE = ((0, 'เห็นด้วยอย่างยิ่ง'), (1, 'เห็นด้วย'), (2, 'ไม่เห็นด้วย'), (3,'ไม่เห็นด้วยอย่างยิ่ง'),)


    gender = models.CharField(max_length=100, choices=gender_CHOICE, null=True)
    name = models.CharField(max_length=255, null=True)
    class_student = models.CharField(max_length=155, choices=class_student_CHOICE, null=True)
    school = models.CharField(max_length=255, null=True)
    school_size = models.CharField(max_length=255, choices=school_size_CHOICE ,null=True)
    short = models.CharField(max_length=255, null=True)
    plan = models.CharField(max_length=255, null=True)
    round_apply = models.CharField(max_length=255, null=True)
    GPA = models.CharField(max_length=50, null=True)
    grade_maths = models.CharField(max_length=50, null=True)
    grade_science = models.CharField(max_length=50, null=True)
    grade_english = models.CharField(max_length=50, null=True)
    GPA_BRU = models.CharField(max_length=255, null=True)
    skillcomputer = models.CharField(max_length=255, choices=ComputerSkillsCompetition_CHOICE, null=True)
    traincomputer = models.CharField(max_length=255, choices=ComputerRelatedtraining_CHOICE, null=True)
    write_program = models.CharField(max_length=255, choices=learnProgramming_CHOICE, null=True)
    trainprogram =models.CharField(max_length=255, choices=programmingTraining_CHOICE, null=True)
    Other_skills = models.TextField(null=True)
    want_to_develop = models.TextField(null=True)
    family_income_per_month = models.CharField(max_length=255, choices=family_income_per_month_CHOICE, null=True)
    status_family = models.CharField(max_length=255, choices=family_status_CHOICE, null=True)
    which_channel_do_you_know = models.TextField(null=True)
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
    
    def plan_no(self):
        if 'วิทย์-คณิต' in self.plan:
            return 5
        elif 'ศิลป์-คำนวณ' in self.plan:
            return 6
        elif 'ศิลป์-ภาษา' in self.plan:
            return 8
        elif 'ประกาศนียบัตรวิชาชีพ(ปวช)' in self.plan:
            return 0
        elif 'ประกาศนียบัตรวิชาชีพขั้นสูง(ปวส)' in self.plan:
            return 1
        elif 'เทียบเท่าละดับมัธยมศึกษาตอนปลาย' in self.plan:
            return 2
        elif 'คณิต-อังกฤษ' in self.plan:
            return 3
        elif 'สังคม-ญี่ปุ่น' in self.plan:
            return 9
        elif "ภาษา สังคม" in self.plan:
            return 4
        else:
            return 7

    def status_family_no(self):
        if 'บิดา มารดาอยู่ด้วยกัน' in self.status_family:
            return 2
        elif 'บิดา มารดาหย่าร้างกัน' in self.status_family:
            return 1
        else:
            return 0
        
    def write_program_no(self):
        if 'ไม่เคย' in self.write_program:
            return 0
        else:
            return 1
        
    def trainprogram_no(self):
        if 'ไม่เคย' in self.trainprogram:
            return 0
        else:
            return 1
        
    def round_apply_no(self):
        if 'portfolio' in self.round_apply:
            return 0
        elif 'นักศึกแลกเปลี่ยน' in self.round_apply:
            return 1
        elif 'รับตรง(เพิ่มเติม)' in self.round_apply:
            return 2
        elif 'รับตรงรอบที่ 1' in self.round_apply:
            return 3
        elif 'รับตรงรอบที่ 2' in self.round_apply:
            return 4
        elif 'รับตรงอิสระ' in self.round_apply:
            return 5
        else :
            return 6
        
    def school_size_no(self):
        if 'รร.ขนาดใหญ่' in self.school_size:
            return 2
        elif 'รร.ขนาดกลาง' in self.school_size:
            return 1
        else:
            return 0
        
    def family_income_per_month_no(self):
        if '10,001 ถึง 15,000 บาท' in self.family_income_per_month:
            return 0
        elif '15,001 ถึง 20,000 บาท' in self.family_income_per_month:
            return 1
        elif '25,001 บาทขึ้นไป' in self.family_income_per_month:
            return 2
        elif '5,001 ถึง 10,000 บาท' in self.family_income_per_month:
            return 3
        elif 'ไม่เกิน 5,000 บาท' in self.family_income_per_month:
            return 4
    class Meta:
        db_table='student'
        verbose_name='นักเรียน'
        verbose_name_plural="ข้อมูลนักเรียน"
        
    