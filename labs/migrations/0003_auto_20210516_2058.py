# Generated by Django 3.2.3 on 2021-05-16 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0002_auto_20210508_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='lab',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
