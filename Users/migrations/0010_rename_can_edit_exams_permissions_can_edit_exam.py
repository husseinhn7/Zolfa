# Generated by Django 4.1.3 on 2022-12-02 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0009_alter_user_age'),
    ]

    operations = [
        migrations.RenameField(
            model_name='permissions',
            old_name='can_edit_exams',
            new_name='can_edit_exam',
        ),
    ]
