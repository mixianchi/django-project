# Generated by Django 2.2.6 on 2019-10-26 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0019_test_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
