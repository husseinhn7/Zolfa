# Generated by Django 4.2.2 on 2023-06-20 13:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Exams', '0008_alter_marks_mark'),
        ('Levels', '0004_remove_subject_exams_remove_subject_subject_level_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=100)),
                ('exams', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Exams.exam')),
                ('subject_level', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Levels.level')),
                ('tutor_name', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_name', models.CharField(default=None, max_length=100, null=True)),
                ('lesson_description', models.TextField()),
                ('lesson_pdf', models.URLField()),
                ('lesson_video', models.URLField()),
                ('subject', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Subjects.subject')),
            ],
        ),
    ]
