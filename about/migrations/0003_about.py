# Generated by Django 3.2 on 2021-05-25 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_rename_about_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('who_we_are', models.TextField(max_length=2000)),
                ('image', models.ImageField(upload_to='about/')),
            ],
        ),
    ]
