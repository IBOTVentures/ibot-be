# Generated by Django 5.1.1 on 2024-10-28 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsappv1', '0017_otp_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]