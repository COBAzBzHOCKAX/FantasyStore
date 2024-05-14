# Generated by Django 5.0.6 on 2024-05-15 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter your title here', max_length=255, verbose_name='Title')),
                ('text', models.TextField(help_text='Enter your text here', verbose_name='Text')),
                ('is_published', models.BooleanField(default=False, verbose_name='Is published')),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')),
                ('date_of_change', models.DateTimeField(auto_now=True, verbose_name='Date of change')),
                ('date_published', models.DateTimeField(blank=True, null=True, verbose_name='Date of publication')),
            ],
            options={
                'verbose_name': 'Ad',
                'verbose_name_plural': 'Ads',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(help_text='Enter your category name here', max_length=255, unique=True, verbose_name='Category name')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
    ]
