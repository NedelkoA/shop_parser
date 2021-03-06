# Generated by Django 2.1 on 2018-08-10 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('brand', models.CharField(max_length=60)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('image', models.URLField()),
            ],
        ),
    ]
