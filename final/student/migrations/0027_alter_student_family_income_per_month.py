# Generated by Django 4.1.3 on 2022-12-29 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0026_alter_student_school_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='family_income_per_month',
            field=models.CharField(choices=[('ไม่เกิน 5,000 บาท', 'ไม่เกิน 5,000 บาท'), ('5,001 – 10,000 บาท', '5,001 – 10,000 บาท'), ('10,001 - 15,000 บาท', '10,001 - 15,000 บาท'), ('15,001 - 20,000 บาท', '15,001 - 20,000 บาท'), ('25,001 บาทขึ้นไป', '25,001 บาทขึ้นไป')], max_length=255, null=True),
        ),
    ]
