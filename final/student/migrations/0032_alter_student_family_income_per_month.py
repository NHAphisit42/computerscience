# Generated by Django 4.1.3 on 2023-01-10 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0031_alter_student_family_income_per_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='family_income_per_month',
            field=models.CharField(choices=[('ไม่เกิน5,000บาท', 'ไม่เกิน5,000บาท'), ('5,001ถึง10,000บาท', '5,001ถึง10,000บาท'), ('10,001ถึง15,000บาท', '10,001ถึง15,000บาท'), ('15,001ถึง20,000 บาท', '15,001ถึง20,000 บาท'), ('25,001บาทขึ้นไป', '25,001บาทขึ้นไป')], max_length=255, null=True),
        ),
    ]