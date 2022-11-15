# Generated by Django 4.0.7 on 2022-10-12 15:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('DONE', 'DONE'), ('INPROGRESS', 'INPROGRESS'), ('NOTSTARTED', 'NOTSTARTED'), ('OTHERS', 'OTHERS')], max_length=255)),
                ('description', models.TextField()),
                ('name', models.TextField(default='')),
                ('enddate', models.DateField(default='2022-10-18')),
                ('updatedate', models.DateField(default='2022-10-18')),
                ('createdate', models.DateField()),
                ('startdate', models.DateField()),
                ('affectedTo', models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='affectedTo', to=settings.AUTH_USER_MODEL)),
                ('creator', models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='creator', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='project', to='project.project')),
            ],
        ),
    ]
