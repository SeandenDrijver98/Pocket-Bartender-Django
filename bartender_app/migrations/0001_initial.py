# Generated by Django 3.2.7 on 2021-09-13 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('instructions', models.TextField(null=True)),
                ('description', models.TextField(null=True)),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('favourite_drinks', models.ManyToManyField(related_name='favourite_users', to='bartender_app.Drink')),
            ],
        ),
        migrations.CreateModel(
            name='UserIngredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_available', models.IntegerField(default=0)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bartender_app.ingredient')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bartender_app.user')),
            ],
        ),
        migrations.CreateModel(
            name='DrinkIngredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_needed', models.IntegerField(default=0)),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bartender_app.drink')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bartender_app.ingredient')),
            ],
        ),
        migrations.AddField(
            model_name='drink',
            name='required_ingredients',
            field=models.ManyToManyField(to='bartender_app.Ingredient'),
        ),
    ]