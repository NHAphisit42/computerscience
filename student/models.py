from unicodedata import name
from django.db import models

PLAN_MAPPING = {
    "วิทย์-คณิต": 5,
    "ศิลป์-คำนวณ": 6,
    "ศิลป์-ภาษา": 8,
    "ประกาศนียบัตรวิชาชีพ(ปวช)": 0,
    "ประกาศนียบัตรวิชาชีพขั้นสูง(ปวส)": 1,
    "เทียบเท่าละดับมัธยมศึกษาตอนปลาย": 2,
    "คณิต-อังกฤษ": 3,
    "ภาษา สังคม": 4,
    "สังคม-ญี่ปุ่น": 9,
}

status_family_no = {
    "บิดา มารดาอยู่ด้วยกัน": 2,
    "บิดา มารดาหย่าร้างกัน": 1,
    "บิดา มารดาไม่ได้อยู่ด้วยกัน": 0
}

write_program_no = {
    "เคย": 1,
    "ไม่เคย": 0
}

trainprogram_no = {
    "เคย": 1,
    "ไม่เคย": 0
}

round_apply_no = {
    "portfolio": 0,
    "นักศึกแลกเปลี่ยน": 1,
    "รับตรง(เพิ่มเติม)": 2,
    "รับตรงรอบที่ 1": 3,
    "รับตรงรอบที่ 2": 4,
    "รับตรงอิสระ": 5
}

school_size_no = {
    "โรงเรียนขนาดใหญ่": 2,
    "โรงเรียนขนาดกลาง": 1,
    "โรงเรียนขนาดเล็ก": 0
}

family_income_per_month_no = {
    "ไม่เกิน 5,000 บาท": 4,
    "5,001 - 10,000 บาท": 3,
    "10,001 - 15,000 บาท": 0,
    "15,001 - 20,000 บาท": 1,
    "25,001 บาทขึ้นไป": 2
}

# Create your models here.
class Student(models.Model):
    GENDER_CHOICES = (
        ("นาย", "นาย"),
        ("นางสาว", "นางสาว"),
        ("นาง", "นาง"),
    )

    class_student_CHOICE = (
        ('รุ่น 61', 'รุ่น 61'), ('รุ่น 62', 'รุ่น 62'), ('รุ่น 63', 'รุ่น 63'), ('รุ่น 64', 'รุ่น 64'),
        ('รุ่น 65', 'รุ่น 65'), ('รุ่น 66', 'รุ่น 66'), ('รุ่น 67', 'รุ่น 67'), ('รุ่น 68', 'รุ่น 68'),
        ('รุ่น 69', 'รุ่น 69'), ('รุ่น 70', 'รุ่น 70'), ('รุ่น 71', 'รุ่น 71'), ('รุ่น 72', 'รุ่น 72'),
        )
    
    SCHOOL_SIZE_CHOICES = (
        ("รร.ขนาดเล็ก", "รร.ขนาดเล็ก"),
        ("รร.ขนาดกลาง", "รร.ขนาดกลาง"),
        ("รร.ขนาดใหญ่", "รร.ขนาดใหญ่"),
    )

    round_apply_CHOICE =(
        ('portfolio', 'portfolio'), ('รับตรงรอบที่ 2', 'รับตรงรอบที่ 2'), ('รับตรงรอบที่ 1', 'รับตรงรอบที่ 1'),
        ('โควต้า', 'โควต้า'), ('รับตรงอิสระ', 'รับตรงอิสระ'), ('นักศึกแลกเปลี่ยน', 'นักศึกแลกเปลี่ยน'), ('รับตรง(เพิ่มเติม)', 'รับตรง(เพิ่มเติม)')
    )
    
    YES_NO_CHOICES = (
        ("เคย", "เคย"),
        ("ไม่เคย", "ไม่เคย"),
    )

    family_income_per_month_CHOICE = (
        ('ไม่เกิน 5,000 บาท', 'ไม่เกิน 5,000 บาท'),
        ('5,001 - 10,000 บาท', '5,001 - 10,000 บาท'),
        ('10,001 - 15,000 บาท', '10,001 - 15,000 บาท'),
        ('15,001 - 20,000 บาท', '15,001 - 20,000 บาท'),
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

    NORMAL_CHOICES = (
        (3, "เห็นด้วยอย่างยิ่ง"),
        (2, "เห็นด้วย"),
        (1, "ไม่เห็นด้วย"),
        (0, "ไม่เห็นด้วยอย่างยิ่ง"),
    )
    
    REVERSE_CHOICES = (
        (0, "เห็นด้วยอย่างยิ่ง"),
        (1, "เห็นด้วย"),
        (2, "ไม่เห็นด้วย"),
        (3, "ไม่เห็นด้วยอย่างยิ่ง"),
    )
    
    id = models.AutoField(primary_key=True, null=False)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, null=True)
    name = models.CharField(max_length=255, null=True)
    class_student = models.CharField(max_length=155, choices=class_student_CHOICE, null=True)
    school = models.CharField(max_length=255, null=True)
    school_size = models.CharField(max_length=255, choices=SCHOOL_SIZE_CHOICES, null=True)
    short = models.CharField(max_length=255, null=True)
    plan = models.CharField(max_length=255, null=True)
    round_apply = models.CharField(max_length=255, choices=round_apply_CHOICE, null=True)
    GPA = models.CharField(max_length=50, null=True)
    grade_maths = models.CharField(max_length=50, null=True)
    grade_science = models.CharField(max_length=50, null=True)
    grade_english = models.CharField(max_length=50, null=True)
    skillcomputer = models.CharField(max_length=255, choices=YES_NO_CHOICES, null=True)
    traincomputer = models.CharField(max_length=255, choices=YES_NO_CHOICES, null=True)
    write_program = models.CharField(max_length=255, choices=YES_NO_CHOICES, null=True)
    trainprogram =models.CharField(max_length=255, choices=YES_NO_CHOICES, null=True)
    Other_skills = models.TextField(null=True)
    want_to_develop = models.TextField(null=True)
    family_income_per_month = models.CharField(max_length=255, choices=family_income_per_month_CHOICE, null=True)
    status_family = models.CharField(max_length=255, choices=family_status_CHOICE, null=True)
    which_channel_do_you_know = models.TextField(null=True)
    why_did_you_choose_to_study = models.TextField(null=True)
    ex1 = models.IntegerField(choices=REVERSE_CHOICES)
    ex2 = models.IntegerField(choices=NORMAL_CHOICES)
    ex3 = models.IntegerField(choices=NORMAL_CHOICES)
    ex4 = models.IntegerField(choices=REVERSE_CHOICES)
    ex5 = models.IntegerField(choices=NORMAL_CHOICES)
    ex6 = models.IntegerField(choices=NORMAL_CHOICES)
    ex7 = models.IntegerField(choices=REVERSE_CHOICES)
    ex8 = models.IntegerField(choices=REVERSE_CHOICES)
    ex9 = models.IntegerField(choices=NORMAL_CHOICES)
    ex10 = models.IntegerField(choices=NORMAL_CHOICES)
    ex11 = models.IntegerField(choices=REVERSE_CHOICES)
    ex12 = models.IntegerField(choices=REVERSE_CHOICES)
    ex13 = models.IntegerField(choices=NORMAL_CHOICES)
    ex14 = models.IntegerField(choices=REVERSE_CHOICES)
    ex15 = models.IntegerField(choices=NORMAL_CHOICES)
    ex16 = models.IntegerField(choices=REVERSE_CHOICES)
    ex17 = models.IntegerField(choices=REVERSE_CHOICES)
    ex18 = models.IntegerField(choices=NORMAL_CHOICES)
    ex19 = models.IntegerField(choices=NORMAL_CHOICES)
    ex20 = models.IntegerField(choices=REVERSE_CHOICES)

    def __str__(self):
        return self.name
    
    def plan_no(self):
        return PLAN_MAPPING.get(self.plan, 7)

    def status_family_no(self):
        return status_family_no.get(self.status_family, 3)
        
    def write_program_no(self):
        return write_program_no.get(self.write_program, 2)
        
    def trainprogram_no(self):
        return trainprogram_no.get(self.trainprogram, 2)
        
    def round_apply_no(self):
        return round_apply_no.get(self.round_apply, 6)
        
    def school_size_no(self):
        return school_size_no.get(self.school_size, 3)
        
    def family_income_per_month_no(self):
        return family_income_per_month_no.get(self.family_income_per_month, 5)
    class Meta:
        db_table='student'
        verbose_name='นักเรียน'
        verbose_name_plural="ข้อมูลนักเรียน"