# Generated by Django 4.0.1 on 2022-02-01 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_alter_eduction_options_alter_plan_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'นักเรียน', 'verbose_name_plural': 'ข้อมูลนักเรียน'},
        ),
        migrations.AlterModelTable(
            name='student',
            table='student',
        ),
    ]