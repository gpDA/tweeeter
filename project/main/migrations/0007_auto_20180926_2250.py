# Generated by Django 2.1.1 on 2018-09-26 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20180926_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='day',
            field=models.CharField(default='day', max_length=300),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='favorite',
            field=models.CharField(default='favorite', max_length=300),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='min',
            field=models.CharField(default='min', max_length=300),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='retweet',
            field=models.CharField(default='retweet', max_length=300),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='year',
            field=models.CharField(default='year', max_length=300),
        ),
    ]
