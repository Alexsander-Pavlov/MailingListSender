# Generated by Django 5.0.6 on 2024-06-17 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail_center', '0004_sendingmessage_slug_alter_sendingmessage_periodicity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendingmessage',
            name='slug',
            field=models.SlugField(max_length=256, null=True),
        ),
    ]
