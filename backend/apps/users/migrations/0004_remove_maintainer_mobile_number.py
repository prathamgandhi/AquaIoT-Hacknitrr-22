# Generated by Django 4.0.3 on 2022-03-05 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_maintainer_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maintainer',
            name='mobile_number',
        ),
    ]
