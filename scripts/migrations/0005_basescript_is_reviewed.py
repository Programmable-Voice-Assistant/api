# Generated by Django 4.1.6 on 2023-02-08 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scripts', '0004_alter_basescript_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='basescript',
            name='is_reviewed',
            field=models.BooleanField(null=True),
        ),
    ]
