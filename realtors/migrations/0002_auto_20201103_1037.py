# Generated by Django 3.1.3 on 2020-11-03 10:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='realtor',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='realtor',
            name='email',
            field=models.CharField(default='contact@immo.com', max_length=50),
        ),
        migrations.AddField(
            model_name='realtor',
            name='hire_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='realtor',
            name='is_mvp',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='realtor',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='realtor',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='realtor',
            name='photo',
            field=models.ImageField(null=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]