# Generated by Django 3.1.1 on 2021-01-02 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20201231_0627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='number',
            field=models.PositiveIntegerField(default=1, null=True),
        ),
    ]
