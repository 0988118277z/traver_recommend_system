# Generated by Django 4.2.8 on 2024-01-11 15:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("RecommenderSystem", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="shopsdata",
            old_name="address",
            new_name="shopAddress",
        ),
        migrations.RenameField(
            model_name="shopsdata",
            old_name="phone",
            new_name="shopPhone",
        ),
    ]
