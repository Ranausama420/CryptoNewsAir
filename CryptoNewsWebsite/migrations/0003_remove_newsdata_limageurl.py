# Generated by Django 3.0.5 on 2020-07-04 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CryptoNewsWebsite', '0002_auto_20200704_2151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsdata',
            name='lImageUrl',
        ),
    ]
