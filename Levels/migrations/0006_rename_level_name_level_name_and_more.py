# Generated by Django 4.2.2 on 2023-06-26 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Levels', '0005_delete_subject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='level',
            old_name='level_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='level',
            name='number_of_students',
        ),
    ]
