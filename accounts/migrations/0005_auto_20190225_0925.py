# Generated by Django 2.1.5 on 2019-02-25 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20190219_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='max_websites',
            field=models.IntegerField(default=0, help_text='maximum number of websites that can be registerd'),
        ),
    ]
