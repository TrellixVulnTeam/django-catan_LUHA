# Generated by Django 3.1.1 on 2020-10-09 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='value',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
