# Generated by Django 4.2.1 on 2023-06-22 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Intakes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intake',
            name='register_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
