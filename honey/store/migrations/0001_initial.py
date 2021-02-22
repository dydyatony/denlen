# Generated by Django 3.1.5 on 2021-01-27 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostsTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('slug', models.SlugField(max_length=65, unique=True, verbose_name='slug')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Title')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True)),
                ('first_photo', models.ImageField(upload_to='photo/%Y/%m/%d', verbose_name='main photo')),
                ('views', models.IntegerField(default=0)),
                ('as_published', models.BooleanField(default=False)),
                ('tags', models.ManyToManyField(related_name='posts', to='store.PostsTags')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ['-created_at'],
            },
        ),
    ]
