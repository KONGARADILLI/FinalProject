# Generated by Django 3.1.7 on 2021-06-01 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlinejobportalApp', '0010_auto_20210601_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_resumes', models.FileField(null=True, upload_to='')),
                ('applied_student', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='recruiter',
            name='applied_student',
        ),
        migrations.RemoveField(
            model_name='recruiter',
            name='tudent_resumes',
        ),
    ]