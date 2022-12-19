# Generated by Django 4.1.2 on 2022-12-16 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Levels', '0003_lesson_lesson_name'),
        ('Exams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='comment',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='exam',
            name='end_date',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='exam',
            name='exam_creator',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='exam',
            name='exam_duration',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='exam',
            name='final',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='exam',
            name='final_mark',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='exam',
            name='start_date',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='exam',
            name='subj',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Levels.subject'),
        ),
        migrations.AddField(
            model_name='exam',
            name='title',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='options',
            name='option',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='options',
            name='question',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Exams.question'),
        ),
        migrations.AddField(
            model_name='question',
            name='exam',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Exams.exam'),
        ),
        migrations.AddField(
            model_name='question',
            name='mark',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='question',
            field=models.TextField(default=None, null=True),
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.IntegerField(default=None, null=True)),
                ('exam', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Exams.exam')),
                ('student', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(default=None, null=True)),
                ('exam', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Exams.exam')),
                ('question', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Exams.question')),
                ('student', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]