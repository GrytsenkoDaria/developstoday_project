# Generated by Django 3.0.6 on 2020-06-02 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_board', '0003_auto_20200602_0957'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Upvote',
        ),
    ]
