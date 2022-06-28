# Generated by Django 4.0.5 on 2022-06-28 17:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_remove_recipeversion_project_recipeproject_recipe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False)),
                ('chef', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
        migrations.RemoveField(
            model_name='recipeversion',
            name='version_number',
        ),
        migrations.AlterField(
            model_name='recipeversion',
            name='chef',
            field=models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, related_name='recipe_versions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='RecipeProject',
        ),
        migrations.AddField(
            model_name='recipe',
            name='recipe',
            field=models.ForeignKey(max_length=255, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to='api.recipeversion'),
        ),
    ]