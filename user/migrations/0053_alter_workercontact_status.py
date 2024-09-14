# Generated by Django 4.2.7 on 2024-08-04 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0052_alter_workercontact_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="workercontact",
            name="status",
            field=models.CharField(
                choices=[
                    ("1 per week", "1 per week"),
                    ("2 per week", "2 per week"),
                    ("3 per week", "3 per week"),
                ],
                max_length=20,
                null=True,
                verbose_name="No of Class weekly",
            ),
        ),
    ]