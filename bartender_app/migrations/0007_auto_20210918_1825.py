# Generated by Django 3.2.7 on 2021-09-18 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bartender_app', '0006_auto_20210918_1817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drink',
            name='ingredients',
        ),
        migrations.RemoveField(
            model_name='drink',
            name='instructions',
        ),
        migrations.AddField(
            model_name='drinkingredient',
            name='drink',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='bartender_app.drink'),
        ),
        migrations.AddField(
            model_name='drinkinstruction',
            name='drink',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='instructions', to='bartender_app.drink'),
        ),
    ]
