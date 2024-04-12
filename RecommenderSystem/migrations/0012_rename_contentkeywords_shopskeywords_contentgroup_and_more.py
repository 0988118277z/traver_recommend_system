# Generated by Django 4.2.8 on 2024-02-04 16:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("RecommenderSystem", "0011_shopskeywords_contentkeywords"),
    ]

    operations = [
        migrations.RenameField(
            model_name="shopskeywords",
            old_name="contentKeyWords",
            new_name="contentGroup",
        ),
        migrations.AddField(
            model_name="shopskeywords",
            name="contentGroupKeys",
            field=models.CharField(max_length=300, null=True),
        ),
    ]
