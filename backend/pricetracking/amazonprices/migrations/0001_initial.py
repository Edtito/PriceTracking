# Generated by Django 3.0.5 on 2020-12-07 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('user', models.CharField(max_length=40)),
            ],
        ),
    ]
