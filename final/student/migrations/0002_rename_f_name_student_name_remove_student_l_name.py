# Generated by Django 4.0 on 2022-01-07 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='f_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='l_name',
        ),
    ]