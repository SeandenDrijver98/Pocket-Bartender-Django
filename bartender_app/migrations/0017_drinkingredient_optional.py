# Generated by Django 4.0.1 on 2022-01-04 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bartender_app", "0016_delete_drinkinstruction"),
    ]

    operations = [
        migrations.AddField(
            model_name="drinkingredient",
            name="optional",
            field=models.BooleanField(default=False),
        ),
    ]