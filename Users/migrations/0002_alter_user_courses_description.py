# Generated by Django 4.1.2 on 2022-12-01 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='courses_description',
            field=models.TextField(default=None, null=True),
        ),
    ]
