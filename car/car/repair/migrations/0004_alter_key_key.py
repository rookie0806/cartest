# Generated by Django 3.2.9 on 2021-12-15 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0003_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='key',
            name='key',
            field=models.CharField(default='', max_length=300),
        ),
    ]
