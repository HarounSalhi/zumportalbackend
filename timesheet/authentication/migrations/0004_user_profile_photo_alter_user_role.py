# Generated by Django 4.1.9 on 2023-10-06 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alter_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_photo',
            field=models.ImageField(default='profile_photos/', upload_to='profile_photos/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('MG', 'manager'), ('SU', 'simple_user'), ('AD', 'admin'), ('TM', 'talent_management'), ('SM', 'SCRUM_MASTER')], default='SU', max_length=2),
        ),
    ]
