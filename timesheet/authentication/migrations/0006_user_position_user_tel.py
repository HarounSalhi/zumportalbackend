# Generated by Django 4.1.9 on 2023-10-07 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_user_dayoffamount_user_ttamount'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='position',
            field=models.CharField(default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='tel',
            field=models.CharField(default='', max_length=255, null=True),
        ),
    ]
