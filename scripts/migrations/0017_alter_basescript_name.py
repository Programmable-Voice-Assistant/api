# Generated by Django 4.1.6 on 2023-03-21 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scripts', '0016_remove_basecommand_parameters_parameters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basescript',
            name='name',
            field=models.TextField(default='_New'),
        ),
    ]
