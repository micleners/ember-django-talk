# Generated by Django 2.2.1 on 2019-05-07 01:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('presenter', models.CharField(blank=True, max_length=256)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('location', models.CharField(blank=True, max_length=256)),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
