# Generated by Django 5.0.6 on 2025-02-13 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='adminuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('username', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=16)),
            ],
        ),
    ]
