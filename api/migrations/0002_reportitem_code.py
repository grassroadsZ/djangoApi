# Generated by Django 2.0.8 on 2018-09-18 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportitem',
            name='code',
            field=models.IntegerField(default=0),
        ),
    ]