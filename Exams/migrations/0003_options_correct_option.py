# Generated by Django 4.1.2 on 2022-12-19 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exams', '0002_exam_comment_exam_end_date_exam_exam_creator_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='options',
            name='correct_option',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
