# Generated by Django 4.2 on 2023-05-03 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gallery", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="artexhibition",
            name="address",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="artexhibition",
            name="source",
            field=models.CharField(max_length=100, null=True),
        ),
    ]