# Generated by Django 4.0.5 on 2022-06-29 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_alter_recipevariation_variation_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipevariation',
            name='variation_number',
            field=models.ForeignKey(max_length=255, on_delete=django.db.models.deletion.CASCADE, related_name='recipe_variations', to='api.recipe'),
        ),
    ]
