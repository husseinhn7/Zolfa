# Generated by Django 4.1.3 on 2022-12-01 19:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_alter_user_is_staff_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permissions',
            name='supervisor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
