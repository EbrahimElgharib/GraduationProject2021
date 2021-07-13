# Generated by Django 3.2.3 on 2021-07-12 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField(max_length=1000)),
            ],
            options={
                'verbose_name': 'FAQ',
                'verbose_name_plural': 'FAQ',
            },
        ),
    ]
