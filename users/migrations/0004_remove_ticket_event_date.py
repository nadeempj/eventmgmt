# Generated by Django 3.2.12 on 2022-02-24 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20220224_1250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='event_date',
        ),
    ]
