# Generated by Django 2.2.6 on 2019-10-24 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0003_dic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dic',
            name='CREATE_TIME',
            field=models.CharField(max_length=200),
        ),
    ]
