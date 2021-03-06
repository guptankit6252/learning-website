# Generated by Django 3.0.3 on 2020-03-19 17:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='mat_solutions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mat_id', models.IntegerField()),
                ('img', models.ImageField(upload_to='pics')),
                ('uploader_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='comments',
            name='yr',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 19, 23, 5, 16, 855991)),
        ),
        migrations.AlterField(
            model_name='materials',
            name='yr',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 19, 23, 5, 16, 819090)),
        ),
    ]
