# Generated by Django 4.0.2 on 2022-02-27 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0029_room_biz_room_eco_room_fam'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.CharField(default='a', max_length=50),
        ),
    ]
