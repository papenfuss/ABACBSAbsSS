# Generated by Django 2.0 on 2018-07-04 08:30

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('demographic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(default=datetime.date.today, verbose_name='Creation date')),
                ('modification_date', models.DateField(default=datetime.date.today, verbose_name='Modification date')),
                ('completed_intial_login', models.BooleanField(default=False)),
                ('email', models.EmailField(default=None, max_length=254, null=True, verbose_name='Email address')),
                ('affiliation', models.CharField(default=None, max_length=64, null=True, verbose_name='Primary Affliation')),
                ('aboriginal_or_torres', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='associated_profiles', to='demographic.AboriginalOrTorres', verbose_name='Do you identify as an Aboriginal or Torres Strait Islander?')),
                ('career_stage', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='associated_profiles', to='demographic.CareerStage', verbose_name='Career Stage')),
                ('gender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='associated_profiles', to='demographic.Gender', verbose_name='Gender')),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='associated_profiles', to='demographic.State', verbose_name='State')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-creation_date'],
                'abstract': False,
            },
        ),
    ]
