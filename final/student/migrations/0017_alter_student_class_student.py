# Generated by Django 4.1.3 on 2022-12-06 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0016_alter_student_class_student_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='class_student',
            field=models.CharField(choices=[('รุ่น61', 'รุ่น61'), ('รุ่น62', 'รุ่น62'), ('รุ่น63', 'รุ่น63'), ('รุ่น64', 'รุ่น64'), ('รุ่น65', 'รุ่น65'), ('รุ่น66', 'รุ่น66'), ('รุ่น67', 'รุ่น67'), ('รุ่น68', 'รุ่น68')], max_length=155, null=True),
        ),
    ]
