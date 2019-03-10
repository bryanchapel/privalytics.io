# Generated by Django 2.1.7 on 2019-03-10 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0003_auto_20190225_1104'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessagesToAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField()),
                ('read', models.BooleanField(default=False)),
                ('read_on', models.DateTimeField()),
            ],
        ),
    ]