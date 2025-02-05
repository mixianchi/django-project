# Generated by Django 2.2.5 on 2019-10-30 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pingshan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appeal',
            name='COMMUNITY_ID',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='appeal',
            name='DISPOSE_UNIT_ID',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='appeal',
            name='DISTRICT_ID',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='appeal',
            name='DISTRICT_NAME',
            field=models.CharField(blank=True, default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='appeal',
            name='EVENT_PROPERTY_ID',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='appeal',
            name='EVENT_SRC_ID',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='appeal',
            name='EVENT_TYPE_ID',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='appeal',
            name='INTIME_ARCHIVE_NUM',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='appeal',
            name='INTIME_TO_ARCHIVE_NUM',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='appeal',
            name='MAIN_TYPE_ID',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='appeal',
            name='OPERATE_NUM',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='appeal',
            name='OVERTIME_ARCHIVE_NUM',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='appeal',
            name='REPORT_NUM',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='appeal',
            name='STREET_ID',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='appeal',
            name='SUB_TYPE_ID',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
