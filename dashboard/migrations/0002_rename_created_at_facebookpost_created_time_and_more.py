# Generated by Django 4.2.6 on 2023-10-10 03:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="facebookpost", old_name="created_at", new_name="created_time",
        ),
        migrations.RenameField(
            model_name="facebookpost", old_name="user", new_name="user_id",
        ),
    ]