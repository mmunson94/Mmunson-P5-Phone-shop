# Generated by Django 4.2.3 on 2024-01-31 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_subscribeusers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SubscribeUsers',
            new_name='SubscribedUsers',
        ),
    ]
