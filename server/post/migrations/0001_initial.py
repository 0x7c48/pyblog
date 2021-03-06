# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-12-06 22:49
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.BigIntegerField()),
                ('changed_by', models.BigIntegerField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('changed_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('login_required', models.NullBooleanField(default=False, help_text='Только для зарег. пользователей')),
                ('password_required', models.NullBooleanField(default=False, help_text='Только с паролем')),
                ('start_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Опубликовать с даты')),
                ('finished_at', models.DateTimeField(blank=True, help_text='Скрыть с даты', null=True)),
                ('language', models.CharField(choices=[('RU', 'RU'), ('EN', 'EN')], default='RU', max_length=255)),
                ('title', models.CharField(help_text='Заголовок', max_length=255)),
                ('slug', models.TextField(help_text='Ссылка')),
                ('redirect', models.TextField(blank=True, help_text='Перенаправить на страницу', null=True)),
                ('template', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(help_text='Описание')),
                ('markdown', models.TextField(blank=True, help_text='Пост', null=True, verbose_name='Пост')),
                ('html', models.TextField(blank=True, help_text='Пост', null=True, verbose_name='Пост')),
                ('content', models.TextField(blank=True, help_text='Контент', null=True)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255), blank=True, default=list, help_text='Через запятую', null=True, size=None)),
                ('rating', models.IntegerField(blank=True, default=0, null=True)),
                ('reviews', models.BigIntegerField(blank=True, default=0, null=True)),
                ('attributes', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Атрибуты', null=True)),
                ('related', models.ManyToManyField(blank=True, related_name='_post_related_+', to='post.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Post',
                'db_table': 'post',
            },
        ),
        migrations.AlterUniqueTogether(
            name='post',
            unique_together=set([('slug', 'language')]),
        ),
    ]
