# Generated by Django 3.1.1 on 2020-09-21 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snacks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='snack',
            name='rank',
            field=models.IntegerField(default=1),
        ),
    ]
