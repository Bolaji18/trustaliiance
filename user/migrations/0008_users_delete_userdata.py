# Generated by Django 4.1.6 on 2023-03-23 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_userdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('duration', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=500)),
                ('contact', models.CharField(max_length=100)),
                ('image1', models.ImageField(upload_to='images/')),
                ('image2', models.ImageField(upload_to='images/')),
                ('image3', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='UserData',
        ),
    ]