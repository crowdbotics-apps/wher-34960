# Generated by Django 2.2.26 on 2022-04-27 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_load_initial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event1', models.CharField(max_length=256)),
                ('event2', models.CharField(max_length=256)),
                ('addEvent', models.BooleanField()),
            ],
        ),
    ]