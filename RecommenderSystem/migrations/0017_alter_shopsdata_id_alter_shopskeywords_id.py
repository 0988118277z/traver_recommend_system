# Generated by Django 4.2.8 on 2024-02-13 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecommenderSystem', '0016_alter_shopsdata_id_alter_shopskeywords_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopsdata',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='shopskeywords',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
