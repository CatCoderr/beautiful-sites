# Generated by Django 4.2.2 on 2023-06-11 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0002_article_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="title",
            field=models.TextField(),
        ),
    ]
