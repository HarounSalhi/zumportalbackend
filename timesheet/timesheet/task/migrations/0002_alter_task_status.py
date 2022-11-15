# Generated by Django 4.0.7 on 2022-10-17 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('COMPLETED', 'COMPLETED'), ('INPROGRESS', 'INPROGRESS'), ('UNSTARTED', 'UNSTARTED'), ('CANCEL', 'CANCEL')], max_length=255),
        ),
    ]
