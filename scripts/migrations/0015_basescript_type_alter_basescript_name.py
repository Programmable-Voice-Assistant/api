# Generated by Django 4.1.6 on 2023-03-17 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scripts', '0014_patterns'),
    ]

    operations = [
        migrations.AddField(
            model_name='basescript',
            name='type',
            field=models.CharField(default='py', max_length=100),
        ),
        migrations.AlterField(
            model_name='basescript',
            name='name',
            field=models.CharField(default='_New', max_length=250),
        ),
    ]
