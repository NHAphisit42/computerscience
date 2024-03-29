# Generated by Django 4.0 on 2022-01-07 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_rename_f_name_student_name_remove_student_l_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='abbreviation',
        ),
        migrations.RemoveField(
            model_name='student',
            name='academic_results',
        ),
        migrations.RemoveField(
            model_name='student',
            name='academic_results_english',
        ),
        migrations.RemoveField(
            model_name='student',
            name='academic_results_mathematics',
        ),
        migrations.RemoveField(
            model_name='student',
            name='academic_results_science',
        ),
        migrations.RemoveField(
            model_name='student',
            name='around',
        ),
        migrations.AddField(
            model_name='student',
            name='grade_english',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='grade_maths',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='grade_science',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='round_apply',
            field=models.CharField(choices=[('portfolio', 'portfolio'), ('โควต้า', 'โควต้า'), ('รับตรงรอบที่ 1 ', 'รับตรงรอบที่ 1 '), ('รับตรงรอบที่ 2 ', 'รับตรงรอบที่ 2 '), ('รับตรง(เพิ่มเติม)', 'รับตรง(เพิ่มเติม)')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='short',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='sophomore_student',
            field=models.CharField(choices=[('ชั้นปีที่ 1', 'ชั้นปีที่ 1'), ('ชั้นปีที่ 2', 'ชั้นปีที่ 2'), ('ชั้นปีที่ 3', 'ชั้นปีที่ 3'), ('ชั้นปีที่ 4', 'ชั้นปีที่ 4')], max_length=155, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='ComputerRelatedtraining',
            field=models.CharField(choices=[('เคย', 'เคย'), ('ไม่เคย', 'ไม่เคย')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='ComputerSkillsCompetition',
            field=models.CharField(choices=[('เคย', 'เคย'), ('ไม่เคย', 'ไม่เคย')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Known_from_any_channel',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Other_skills',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='family_income_per_month',
            field=models.CharField(choices=[('ไม่เกิน 5,000 บาท', 'ไม่เกิน 5,000 บาท'), ('5,001 ถึง 10,000 บาท', '5,001 ถึง 10,000 บาท'), ('10,001 ถึง 15,000 บาท', '10,001 ถึง 15,000 บาท'), ('15,001 ถึง 20,000 บาท', '15,001 ถึง 20,000 บาท'), ('25,001 บาทขึ้นไป', '25,001 บาทขึ้นไป')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='family_status',
            field=models.CharField(choices=[('บิดา มารดาอยู่ด้วยกัน', 'บิดา มารดาอยู่ด้วยกัน'), ('บิดา มารดาหย่าร้างกัน', 'บิดา มารดาหย่าร้างกัน'), ('บิดาถึงแก่กรรม', 'บิดาถึงแก่กรรม'), ('มารดาถึงแก่กรรม', 'มารดาถึงแก่กรรม'), ('อยู่กับบิดา', 'อยู่กับบิดา'), ('อยู่กับมารดา', 'อยู่กับมารดา')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('นาย', 'นาย'), ('นางสาว', 'นางสาว'), ('นาง', 'นาง')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='improve_skills',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='learnProgramming',
            field=models.CharField(choices=[('เคย', 'เคย'), ('ไม่เคย', 'ไม่เคย')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='plan',
            field=models.CharField(choices=[('แผนกการเรียน วิทย์-คณิต', 'แผนกการเรียน วิทย์-คณิต'), ('แผนกการเรียน ศิลป์-คำนวณ', 'แผนกการเรียน ศิลป์-คำนวณ'), ('แผนกการเรียน ศิลป์-ภาษา', 'แผนกการเรียน ศิลป์-ภาษา'), ('แผนกการเรียน คณิตศาสตร์-ภาษาอังกฤษ', 'แผนกการเรียน คณิตศาสตร์-ภาษาอังกฤษ'), ('แผนกการเรียน ภาษา-สังคม', 'แผนกการเรียน ภาษา-สังคม'), ('แผนกการเรียน สังคม-ญี่ปุ่น', 'แผนกการเรียน ภาษา-ญี่ปุ่น'), ('ประกาศนียบัตรวิชาชีพ(ปวช)', 'ประกาศนียบัตรวิชาชีพ(ปวช)'), ('ประกาศนียบัตรวิชาชีพขั้นสูง(ปวส)', 'ประกาศนียบัตรวิชาชีพขั้นสูง(ปวส)'), ('เทียบเท่าละดับมัธยมศึกษาตอนปลาย)', 'เทียบเท่าละดับมัธยมศึกษาตอนปลาย')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='programmingTraining',
            field=models.CharField(choices=[('เคย', 'เคย'), ('ไม่เคย', 'ไม่เคย')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='school',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='why_did_you_choose_to_study',
            field=models.TextField(null=True),
        ),
    ]
