# Generated by Django 3.2.8 on 2021-10-21 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game_app', '0004_auto_20211019_1708'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recordslist',
            options={'ordering': ['-record']},
        ),
        migrations.AlterField(
            model_name='shoplist',
            name='item_mame',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game_app.itemlist'),
        ),
    ]
