# Generated by Django 4.0.5 on 2022-07-07 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_alter_recipeversion_ingredients_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Ingredient',
        ),
        migrations.RemoveField(
            model_name='recipeversion',
            name='version_number',
        ),
    ]
