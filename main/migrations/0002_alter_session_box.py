# Generated by Django 4.2.4 on 2023-08-18 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='box',
            field=models.TextField(blank=True, help_text='The current box at its latest state', null=True, verbose_name='Box'),
        ),
    ]
