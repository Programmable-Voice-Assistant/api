# Generated by Django 4.1.6 on 2023-03-14 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scripts', '0013_basecommand_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patterns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('syntax', models.TextField()),
                ('command', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scripts.basecommand')),
            ],
        ),
    ]