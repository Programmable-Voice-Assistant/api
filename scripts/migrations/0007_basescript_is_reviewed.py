# Generated by Django 4.1.6 on 2023-02-18 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scripts', '0006_remove_basescript_is_reviewed'),
    ]

    operations = [
        migrations.AddField(
            model_name='basescript',
            name='is_reviewed',
            field=models.BooleanField(null=True),
        ),
    ]
