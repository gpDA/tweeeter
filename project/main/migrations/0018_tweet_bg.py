# Generated by Django 2.1.1 on 2018-09-27 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_remove_tweet_bg'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='bg',
            field=models.URLField(default='https://www.cbronline.com/wp-content/uploads/2016/06/twitter2.png', max_length=500),
        ),
    ]