# Generated by Django 3.2.8 on 2021-10-21 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_app', '0005_auto_20211021_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoplist',
            name='item_mame',
            field=models.CharField(max_length=200),
        ),
    ]
