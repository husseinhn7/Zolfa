# Generated by Django 4.1.2 on 2022-12-01 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Levels', '0002_subject_tutor_name'),
        ('Users', '0002_alter_user_courses_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='intake',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.intake'),
        ),
        migrations.AlterField(
            model_name='user',
            name='level',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Levels.level'),
        ),
    ]
