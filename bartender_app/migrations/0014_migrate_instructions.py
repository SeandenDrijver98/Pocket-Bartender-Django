from django.db import migrations, models


def migrate_instructions(apps, schema_editor):
    DrinkInstruction = apps.get_model('bartender_app', 'DrinkInstruction')
    Drink = apps.get_model('bartender_app', 'Drink')

    for drink in Drink.objects.all():
        drink_instruction = ""
        for instruction in DrinkInstruction.objects.filter(drink_id=drink.id).values_list('title',flat=True):
            drink_instruction += str(instruction)+"/n"
            drink.instructions = "".join(drink_instruction)
            drink.save()



class Migration(migrations.Migration):

    dependencies = [
        ('bartender_app', '0013_auto_20211017_1521'),
    ]

    operations = [
        migrations.RunPython(migrate_instructions)
    ]
