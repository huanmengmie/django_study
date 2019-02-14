# Generated by Django 2.1.7 on 2019-02-13 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('author', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('pub_date', models.TimeField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]
