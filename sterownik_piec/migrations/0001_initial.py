# Generated by Django 2.2.17 on 2020-12-18 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Czujniki',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=20)),
                ('wartosc', models.FloatField()),
                ('typ', models.CharField(max_length=1)),
            ],
        ),
    ]
