# Generated by Django 3.2.4 on 2021-08-02 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0002_auto_20210628_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='text',
            field=models.CharField(max_length=3000, null=True),
        ),
    ]
