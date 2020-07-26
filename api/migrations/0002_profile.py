# Generated by Django 3.0.8 on 2020-07-26 10:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=15)),
                ('lastname', models.CharField(max_length=15)),
                ('username', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=40)),
                ('country', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=15)),
                ('registered_on', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.
                                              deletion.CASCADE,
                                              to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
