# Generated by Django 3.2.8 on 2021-10-17 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bartender_app', '0012_auto_20211001_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='drink',
            name='instructions',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='drinkinstruction',
            name='drink',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='instructions_linked', to='bartender_app.drink'),
        ),
    ]
