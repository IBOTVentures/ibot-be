# Generated by Django 5.1.2 on 2025-01-02 09:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsappv1', '0006_cartdata_created_at_cartdata_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartdata',
            name='transact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_transaction', to='lmsappv1.transaction'),
        ),
    ]
