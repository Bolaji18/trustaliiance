# Generated by Django 4.2.7 on 2023-11-25 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0033_remove_workers_random_id_worker_randoms"),
    ]

    operations = [
        migrations.AddField(
            model_name="services",
            name="randoms",
            field=models.IntegerField(null=True),
        ),
    ]
