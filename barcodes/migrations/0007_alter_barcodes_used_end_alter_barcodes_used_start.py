# Generated by Django 4.1.7 on 2024-02-10 05:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barcodes', '0006_alter_barcodes_used_end_alter_barcodes_used_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barcodes',
            name='used_end',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 13, 5, 36, 32, 70947, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='barcodes',
            name='used_start',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 11, 5, 36, 32, 70338, tzinfo=datetime.timezone.utc)),
        ),
    ]
