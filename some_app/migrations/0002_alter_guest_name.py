# Generated by Django 5.0.4 on 2024-05-04 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("some_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="guest",
            name="name",
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
