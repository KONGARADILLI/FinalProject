# Generated by Django 3.1.7 on 2021-05-31 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlinejobportalApp', '0004_auto_20210531_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='salary',
            field=models.FloatField(null=True),
        ),
    ]