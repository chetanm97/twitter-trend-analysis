# Generated by Django 2.1.7 on 2019-04-09 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_delete_hash_class'),
    ]

    operations = [
        migrations.CreateModel(
            name='polarity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pos_bjp', models.IntegerField()),
                ('pos_cong', models.IntegerField()),
                ('neg_bjp', models.IntegerField()),
                ('neg_cong', models.IntegerField()),
                ('total', models.IntegerField()),
            ],
        ),
    ]
