# Generated by Django 3.2.3 on 2021-07-02 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0003_auto_20210702_0443'),
    ]

    operations = [
        migrations.AddField(
            model_name='lab',
            name='youtube_url',
            field=models.URLField(null=True),
        ),
    ]