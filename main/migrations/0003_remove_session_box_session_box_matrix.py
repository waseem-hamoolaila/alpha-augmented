# Generated by Django 4.2.4 on 2023-08-18 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_session_box'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='box',
        ),
        migrations.AddField(
            model_name='session',
            name='box_matrix',
            field=models.TextField(blank=True, help_text='The current box at its latest state', null=True, verbose_name='Box'),
        ),
    ]
