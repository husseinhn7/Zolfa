# Generated by Django 4.2.1 on 2023-05-14 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Exams', '0006_alter_answers_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='exam',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Exams.exam'),
        ),
        migrations.AlterField(
            model_name='marks',
            name='mark',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
