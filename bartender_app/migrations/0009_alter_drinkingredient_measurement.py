# Generated by Django 3.2.7 on 2021-09-18 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bartender_app', '0008_alter_drinkingredient_quantity_needed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drinkingredient',
            name='measurement',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
