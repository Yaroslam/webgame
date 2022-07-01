# Generated by Django 3.2.8 on 2022-04-06 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_app', '0012_heroeslist_hero_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='LevelList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_name', models.TextField()),
                ('level_dif', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='itemlist',
            old_name='item_mame',
            new_name='item_name',
        ),
    ]
