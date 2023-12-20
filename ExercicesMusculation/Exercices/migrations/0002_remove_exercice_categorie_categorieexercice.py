# Generated by Django 4.2.8 on 2023-12-20 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Exercices', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercice',
            name='categorie',
        ),
        migrations.CreateModel(
            name='CategorieExercice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Exercices.categorie')),
                ('exercice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Exercices.exercice')),
            ],
        ),
    ]
