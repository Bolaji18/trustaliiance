# Generated by Django 4.2.5 on 2023-11-15 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0027_services_local_govt_alter_services_contact_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="services",
            name="image1",
        ),
        migrations.RemoveField(
            model_name="services",
            name="image2",
        ),
    ]