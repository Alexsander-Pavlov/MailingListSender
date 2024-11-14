# Generated by Django 5.0.6 on 2024-06-22 21:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='название поста')),
                ('image_user', models.ImageField(blank=True, null=True, upload_to='post_users/%Y/%m/%d/', verbose_name='картинка пользователя')),
                ('image', models.ImageField(blank=True, null=True, upload_to='posts/%Y/%m/%d/', verbose_name='картинка')),
                ('description', models.TextField(verbose_name='описание')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('views', models.PositiveIntegerField(default=0, editable=False, verbose_name='просмотры')),
                ('likes', models.IntegerField(default=0, verbose_name='лайки')),
                ('time_published', models.DateTimeField(auto_now_add=True, verbose_name='дата публикации')),
                ('time_edit', models.DateTimeField(blank=True, null=True, verbose_name='дата измененения')),
                ('is_edit', models.BooleanField(default=False)),
                ('text_to_edit', models.CharField(default='Изменено:', max_length=50)),
                ('comment_count', models.IntegerField(default=0, verbose_name='количество комментариев')),
                ('is_published', models.BooleanField(default=True)),
                ('name_button', models.CharField(default='Посмотреть', max_length=50, verbose_name='имя кнопки')),
                ('name_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='имя пользователя')),
            ],
            options={
                'verbose_name': 'пост',
                'verbose_name_plural': 'посты',
                'ordering': ['-time_published'],
            },
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='post_users/%Y/%m/%d/', verbose_name='картинка')),
                ('text', models.TextField(blank=True, null=True, verbose_name='описание')),
                ('time_published', models.DateTimeField(auto_now_add=True, verbose_name='дата публикации')),
                ('time_edit', models.DateTimeField(auto_now=True, verbose_name='дата измененения')),
                ('is_edit', models.BooleanField(default=False)),
                ('text_to_edit', models.CharField(default='Изменено:', max_length=50)),
                ('likes', models.IntegerField(default=0, verbose_name='лайки')),
                ('is_published', models.BooleanField(default=True)),
                ('user_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='postcomment', to=settings.AUTH_USER_MODEL, verbose_name='имя пользователя')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.posts', verbose_name='имя поста')),
            ],
            options={
                'verbose_name': 'комментарий',
                'verbose_name_plural': 'комментарии',
                'ordering': ['-time_published'],
            },
        ),
    ]
