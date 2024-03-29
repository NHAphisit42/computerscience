# Generated by Django 4.0.1 on 2022-02-01 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_alter_student_ex1_alter_student_ex10_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eduction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Round_apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_apply_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_school', models.CharField(max_length=255)),
                ('size_school', models.CharField(max_length=255)),
                ('zone_school', models.CharField(max_length=255)),
                ('district_school', models.CharField(max_length=255)),
                ('province_school', models.CharField(max_length=255)),
                ('Latitude', models.CharField(max_length=255)),
                ('Longitude', models.CharField(max_length=255)),
            ],
        ),
    ]
