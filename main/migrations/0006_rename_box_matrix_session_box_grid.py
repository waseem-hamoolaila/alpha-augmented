# Generated by Django 4.2.4 on 2023-08-20 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_session_id_alter_session_uuid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='session',
            old_name='box_matrix',
            new_name='box_grid',
        ),
    ]