# Generated by Django 4.2.5 on 2023-10-30 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0014_alter_users_duration"),
    ]

    operations = [
        migrations.DeleteModel(
            name="UploadImage",
        ),
    ]