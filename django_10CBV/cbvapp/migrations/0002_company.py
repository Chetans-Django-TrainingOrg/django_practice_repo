# Generated by Django 3.1.5 on 2021-02-08 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbvapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('ceo', models.CharField(max_length=30)),
            ],
        ),
    ]