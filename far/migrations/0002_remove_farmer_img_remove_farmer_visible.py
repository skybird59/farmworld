# Generated by Django 4.1.2 on 2022-11-28 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("far", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="farmer", name="img",),
        migrations.RemoveField(model_name="farmer", name="visible",),
    ]
