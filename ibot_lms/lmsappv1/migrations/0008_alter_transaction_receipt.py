# Generated by Django 5.1.2 on 2025-01-02 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsappv1', '0007_alter_cartdata_transact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='receipt',
            field=models.CharField(blank=True, null=True, unique=True),
        ),
    ]
