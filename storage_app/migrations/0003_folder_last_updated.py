# Generated by Django 4.2.13 on 2024-08-17 16:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("storage_app", "0002_file"),
    ]

    operations = [
        migrations.AddField(
            model_name="folder",
            name="last_updated",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
