# Generated by Django 4.0.7 on 2022-10-28 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_alter_task_updatedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='updatedate',
            field=models.DateField(),
        ),
    ]