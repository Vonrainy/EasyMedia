# Generated by Django 3.1.7 on 2021-03-31 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=20, unique=True)),
                ('username', models.CharField(max_length=20)),
                ('user_place', models.CharField(max_length=20)),
                ('userToken', models.CharField(max_length=50)),
            ],
        ),
    ]
