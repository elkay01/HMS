# Generated by Django 4.0.2 on 2022-02-26 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0028_auto_20220112_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='biz',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='eco',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='fam',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
