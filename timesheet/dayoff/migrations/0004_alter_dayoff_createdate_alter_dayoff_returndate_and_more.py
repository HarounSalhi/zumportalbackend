# Generated by Django 4.1.9 on 2023-09-24 10:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dayoff', '0003_alter_dayoff_createdate_alter_dayoff_motif_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dayoff',
            name='createdate',
            field=models.DateField(default=datetime.date(2023, 9, 24)),
        ),
        migrations.AlterField(
            model_name='dayoff',
            name='returndate',
            field=models.DateField(default=datetime.date(2023, 9, 24)),
        ),
        migrations.AlterField(
            model_name='dayoff',
            name='startdate',
            field=models.DateField(default=datetime.date(2023, 9, 24)),
        ),
    ]
