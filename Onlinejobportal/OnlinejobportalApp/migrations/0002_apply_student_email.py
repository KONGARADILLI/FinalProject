# Generated by Django 3.1.7 on 2021-06-03 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlinejobportalApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='student_email',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
