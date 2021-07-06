# Generated by Django 3.2 on 2021-05-08 03:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='users_image/')),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('education', models.CharField(blank=True, choices=[('ES', 'Elementary School'), ('MS', 'Middle School'), ('HS', 'High School'), ('U', 'University'), ('G', 'Graduate')], max_length=2, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
