# Generated by Django 2.2.5 on 2019-10-30 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pingshan', '0002_auto_20191030_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appeal',
            name='COMMUNITY_NAME',
            field=models.CharField(blank=True, default='-', max_length=20),
        ),
        migrations.AlterField(
            model_name='appeal',
            name='DISPOSE_UNIT_NAME',
            field=models.CharField(blank=True, default='-', max_length=40),
        ),
        migrations.AlterField(
            model_name='appeal',
            name='DISTRICT_NAME',
            field=models.CharField(blank=True, default='-', max_length=20),
        ),
        migrations.AlterField(
            model_name='appeal',
            name='EVENT_PROPERTY_NAME',
            field=models.CharField(blank=True, default='-', max_length=20),
        ),
        migrations.AlterField(
            model_name='appeal',
            name='EVENT_SRC_NAME',
            field=models.CharField(blank=True, default='-', max_length=20),
        ),
        migrations.AlterField(
            model_name='appeal',
            name='EVENT_TYPE_NAME',
            field=models.CharField(blank=True, default='-', max_length=20),
        ),
        migrations.AlterField(
            model_name='appeal',
            name='MAIN_TYPE_NAME',
            field=models.CharField(blank=True, default='-', max_length=20),
        ),
        migrations.AlterField(
            model_name='appeal',
            name='OCCUR_PLACE',
            field=models.CharField(blank=True, default='-', max_length=20),
        ),
        migrations.AlterField(
            model_name='appeal',
            name='STREET_NAME',
            field=models.CharField(blank=True, default='-', max_length=20),
        ),
        migrations.AlterField(
            model_name='appeal',
            name='SUB_TYPE_NAME',
            field=models.CharField(blank=True, default='-', max_length=40),
        ),
    ]
