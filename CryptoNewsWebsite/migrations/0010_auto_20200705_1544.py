# Generated by Django 3.0.5 on 2020-07-05 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CryptoNewsWebsite', '0009_auto_20200705_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsdata',
            name='publishedAt',
            field=models.TextField(),
        ),
    ]
