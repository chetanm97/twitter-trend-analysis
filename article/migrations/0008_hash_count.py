# Generated by Django 2.1.7 on 2019-05-05 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_auto_20190411_1214'),
    ]

    operations = [
        migrations.CreateModel(
            name='hash_count',
            fields=[
                ('hashtag', models.IntegerField(primary_key=True, serialize=False)),
                ('count', models.IntegerField()),
            ],
        ),
    ]
