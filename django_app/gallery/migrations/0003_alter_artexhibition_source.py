# Generated by Django 4.2.2 on 2023-06-06 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gallery", "0002_artexhibition_address_artexhibition_source"),
    ]

    operations = [
        migrations.AlterField(
            model_name="artexhibition",
            name="source",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
