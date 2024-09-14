# Generated by Django 4.2.7 on 2024-08-17 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0054_alter_workercontact_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="workercontact",
            name="status",
            field=models.CharField(
                choices=[("1", "1"), ("2", "2"), ("3", "3")],
                max_length=20,
                null=True,
                verbose_name="No of Jobs",
            ),
        ),
    ]
