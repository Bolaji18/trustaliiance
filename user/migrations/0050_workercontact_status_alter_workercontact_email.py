# Generated by Django 4.2.7 on 2024-07-30 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0049_workercontact_location_workercontact_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="workercontact",
            name="status",
            field=models.CharField(
                choices=[
                    ("1 per week", "1 per week"),
                    ("2 per week", "2 per week"),
                    ("3 per week", "3 per week"),
                ],
                default=1,
                max_length=20,
                verbose_name="No of Classes",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="workercontact",
            name="email",
            field=models.CharField(max_length=50, null=True, verbose_name="Email"),
        ),
    ]