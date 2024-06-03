# Generated by Django 5.0.6 on 2024-05-20 21:21

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_avatar_alter_user_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='steam_url_profile',
            field=models.URLField(blank=True, help_text='Enter your Steam profile URL', max_length=255, null=True, verbose_name='Your Steam account'),
        ),
        migrations.AddField(
            model_name='user',
            name='telegram_nickname',
            field=models.CharField(blank=True, help_text='Specify the nickname "telegram". Only letters from A to Z, numbers 0-9, _. Example: QweRty_123', max_length=255, null=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='Your telegram nickname'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/', verbose_name='Avatar'),
        ),
        migrations.AlterField(
            model_name='user',
            name='discord_url_profile',
            field=models.URLField(blank=True, help_text='Enter your Discord profile URL', max_length=255, null=True, verbose_name='Your Discord account'),
        ),
    ]