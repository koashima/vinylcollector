# Generated by Django 3.0.4 on 2020-05-07 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_contributor'),
    ]

    operations = [
        migrations.AddField(
            model_name='vinyl',
            name='contributors',
            field=models.ManyToManyField(to='main_app.Contributor'),
        ),
    ]