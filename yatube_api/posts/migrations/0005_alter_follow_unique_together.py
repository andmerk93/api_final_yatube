# Generated by Django 4.1.5 on 2023-01-11 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_rename_author_follow_following_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together=set(),
        ),
    ]
