# Generated by Django 3.2.9 on 2022-01-03 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0004_alter_key_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='repair',
            name='date',
        ),
        migrations.RemoveField(
            model_name='repair',
            name='phone_number',
        ),
    ]
