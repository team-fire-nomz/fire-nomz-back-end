# Generated by Django 4.0.5 on 2022-06-21 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_note_recipeversion_tag_tasterfeedback_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
    ]
