# Generated by Django 4.1.3 on 2022-12-01 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0005_alter_permissions_supervisor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='courses',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='education',
            field=models.CharField(max_length=70, null=True),
        ),
    ]
