# Generated by Django 4.2 on 2023-05-15 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Receta_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='poster',
            field=models.ImageField(upload_to='posters/'),
        ),
    ]