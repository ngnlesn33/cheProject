# Generated by Django 4.2.4 on 2023-08-28 06:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("che_project_app", "0004_alter_car_fuel"),
    ]

    operations = [
        migrations.AddField(
            model_name="purpose",
            name="type",
            field=models.IntegerField(default=1),
        ),
    ]
