# Generated by Django 4.0 on 2023-03-23 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_notas'),
    ]

    operations = [
        migrations.AddField(
            model_name='notas',
            name='descripcion',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]