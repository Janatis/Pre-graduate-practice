# Generated by Django 5.1.3 on 2024-12-03 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education_programm',
            name='SUBJECTS',
        ),
        migrations.AddField(
            model_name='education_programm',
            name='SUBJECTS',
            field=models.ManyToManyField(to='education.subject', verbose_name='Предметы'),
        ),
    ]
