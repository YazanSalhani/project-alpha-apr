# Generated by Django 5.0.6 on 2024-05-28 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0002_task"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Task",
        ),
    ]
