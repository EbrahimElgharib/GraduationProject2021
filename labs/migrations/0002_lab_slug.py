# Generated by Django 3.2.3 on 2021-07-02 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lab',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]