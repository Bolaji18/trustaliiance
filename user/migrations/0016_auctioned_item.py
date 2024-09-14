# Generated by Django 4.2.5 on 2023-10-31 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0015_delete_uploadimage"),
    ]

    operations = [
        migrations.CreateModel(
            name="auctioned_item",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("item_description", models.CharField(max_length=100)),
                ("item_price", models.IntegerField()),
                ("item_bid", models.IntegerField()),
                ("email", models.CharField(max_length=100)),
                ("image1", models.ImageField(upload_to="images/")),
                ("image2", models.ImageField(upload_to="images/")),
                ("image3", models.ImageField(upload_to="images/")),
                ("image4", models.ImageField(upload_to="images/")),
                ("image5", models.ImageField(upload_to="images/")),
            ],
        ),
    ]
