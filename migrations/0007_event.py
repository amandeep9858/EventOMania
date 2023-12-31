# Generated by Django 5.0 on 2023-12-05 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0006_auto_20200212_1624'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date', models.DateTimeField()),
                ('location', models.CharField(max_length=255)),
            ],
        ),
    ]
