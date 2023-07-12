# Generated by Django 4.2 on 2023-06-30 23:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scripts', '0021_remove_commandapproverequest_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='basecommand',
            name='used_by',
            field=models.ManyToManyField(related_name='used_by', to=settings.AUTH_USER_MODEL),
        ),
    ]