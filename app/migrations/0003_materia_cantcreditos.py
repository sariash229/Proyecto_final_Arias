# Generated by Django 4.0 on 2023-03-13 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_materia'),
    ]

    operations = [
        migrations.AddField(
            model_name='materia',
            name='cantCreditos',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]