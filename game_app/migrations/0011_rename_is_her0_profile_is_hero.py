# Generated by Django 3.2.8 on 2021-10-21 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game_app', '0010_auto_20211021_2326'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='is_her0',
            new_name='is_hero',
        ),
    ]
