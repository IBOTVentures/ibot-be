# Generated by Django 5.1.1 on 2024-10-09 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsappv1', '0006_remove_module_overview_module_intro_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='isconfirmed',
            field=models.BooleanField(default=False),
        ),
    ]
