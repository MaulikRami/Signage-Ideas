# Generated by Django 5.1.7 on 2025-03-21 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_service_delete_testcase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]
