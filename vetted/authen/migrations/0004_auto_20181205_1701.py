# Generated by Django 2.1.4 on 2018-12-05 17:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0003_adminprofileinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminprofileinfo',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authen.CompanyInfo'),
        ),
        migrations.AlterField(
            model_name='adminprofileinfo',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]