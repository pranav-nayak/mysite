# Generated by Django 2.1.5 on 2019-10-29 06:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20191029_0658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 29, 6, 58, 23, 407528), verbose_name='date published'),
        ),
    ]
