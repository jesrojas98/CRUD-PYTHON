# Generated by Django 5.0.6 on 2024-06-15 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='nombre',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
