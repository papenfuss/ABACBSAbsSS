# Generated by Django 2.0 on 2018-07-04 08:30

import abstract.validators
import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import functools


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Abstract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(default=datetime.date.today, verbose_name='Creation date')),
                ('modification_date', models.DateField(default=datetime.date.today, verbose_name='Modification date')),
                ('text', models.TextField(default=None, help_text='Your abstract is limited 250 words or less and is judged strictly based on the merit of its scientific content, ability to engage the judging panel and your contribution to the work.', validators=[functools.partial(abstract.validators.validate_n_word_or_less, *(), **{'n': 250})], verbose_name='Abstract')),
                ('title', models.TextField(default=None, help_text='Please title your abstract using 20 words or less.', validators=[functools.partial(abstract.validators.validate_n_word_or_less, *(), **{'n': 20})], verbose_name='Abstract title')),
                ('contribution', models.TextField(default=None, help_text='Please describe your contribution to the work described in your abstract using 100 words or less.', validators=[functools.partial(abstract.validators.validate_n_word_or_less, *(), **{'n': 100})], verbose_name='Your contribution')),
                ('authors', models.TextField(blank=True, default=None, help_text='Please list all other contributing authors (comma separated).', verbose_name='Contributing authors')),
                ('author_affiliations', models.TextField(blank=True, default=None, help_text='Please list the primary affiliations of all other contributing authors (comma separated).', verbose_name='Contributing author affiliations')),
            ],
            options={
                'ordering': ('-creation_date',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(default=datetime.date.today, verbose_name='Creation date')),
                ('modification_date', models.DateField(default=datetime.date.today, verbose_name='Modification date')),
                ('text', models.TextField(default=None, verbose_name='Comment')),
                ('score_content', models.IntegerField(default=None, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name="Score based on the abstract's scientific content.")),
                ('score_contribution', models.IntegerField(default=None, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name="Score based on the author's contribution to the work.")),
                ('score_interest', models.IntegerField(default=None, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name="Score based on the ability of the abstract's contents to hold your interest.")),
                ('abstract', models.ForeignKey(blank=None, on_delete=django.db.models.deletion.CASCADE, related_name='comments', related_query_name='comment', to='abstract.Abstract')),
                ('reviewer', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='comments', related_query_name='comment', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('reviewer',),
            },
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(default=datetime.date.today, verbose_name='Creation date')),
                ('modification_date', models.DateField(default=datetime.date.today, verbose_name='Modification date')),
                ('text', models.CharField(default=None, max_length=128, unique=True)),
            ],
            options={
                'ordering': ('text',),
            },
        ),
        migrations.CreateModel(
            name='PresentationCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(default=datetime.date.today, verbose_name='Creation date')),
                ('modification_date', models.DateField(default=datetime.date.today, verbose_name='Modification date')),
                ('name', models.CharField(default=None, max_length=128, unique=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='abstract',
            name='categories',
            field=models.ManyToManyField(help_text='Please select one or more categories for your abstract.', related_name='abstracts', related_query_name='abstract', to='abstract.PresentationCategory', verbose_name='Categories'),
        ),
        migrations.AddField(
            model_name='abstract',
            name='keywords',
            field=models.ManyToManyField(help_text='Please assign a few keywords to your abstract. You may enterkeywords that do not appear in this list.', related_name='abstracts', related_query_name='abstract', to='abstract.Keyword', verbose_name='Keywords'),
        ),
        migrations.AddField(
            model_name='abstract',
            name='reviewers',
            field=models.ManyToManyField(related_name='assigned_abstracts', related_query_name='abstract', to=settings.AUTH_USER_MODEL, verbose_name='Assign reviewers'),
        ),
        migrations.AddField(
            model_name='abstract',
            name='submitter',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='abstracts', related_query_name='abstract', to=settings.AUTH_USER_MODEL, verbose_name='Submitter'),
        ),
        migrations.AlterUniqueTogether(
            name='comment',
            unique_together={('reviewer', 'abstract')},
        ),
    ]