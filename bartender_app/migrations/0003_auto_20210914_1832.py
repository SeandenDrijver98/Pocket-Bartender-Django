# Generated by Django 3.2.7 on 2021-09-14 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bartender_app', '0002_auto_20210914_1823'),
    ]

    operations = [
        migrations.CreateModel(
            name='DrinkIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_needed', models.IntegerField(default=0)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bartender_app.ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='UserIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_available', models.IntegerField(default=0)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bartender_app.ingredient')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bartender_app.user')),
            ],
        ),
        migrations.RemoveField(
            model_name='useringredients',
            name='ingredient',
        ),
        migrations.RemoveField(
            model_name='useringredients',
            name='user',
        ),
        migrations.DeleteModel(
            name='DrinkIngredients',
        ),
        migrations.DeleteModel(
            name='UserIngredients',
        ),
        migrations.AddField(
            model_name='drink',
            name='required_ingredients',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bartender_app.drinkingredient'),
        ),
    ]
