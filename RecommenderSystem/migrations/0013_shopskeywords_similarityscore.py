# Generated by Django 4.2.8 on 2024-02-05 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecommenderSystem', '0012_rename_contentkeywords_shopskeywords_contentgroup_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopskeywords',
            name='similarityScore',
            field=models.FloatField(null=True),
        ),
    ]