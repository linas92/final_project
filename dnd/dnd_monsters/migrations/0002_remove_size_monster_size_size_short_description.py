# Generated by Django 4.1.3 on 2022-12-07 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd_monsters', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='size',
            name='monster_size',
        ),
        migrations.AddField(
            model_name='size',
            name='short_description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]