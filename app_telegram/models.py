from django.db import models
from django.conf import settings


class TelegramUser(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    username = models.CharField(max_length=32, null=True, blank=True, default='', verbose_name='username')
    first_name = models.CharField(max_length=70, null=True, blank=True, default='', verbose_name='first name')
    last_name = models.CharField(max_length=70, null=True, blank=True, default='', verbose_name='last name')
    phone = models.CharField(max_length=20, null=True, blank=True, default='', verbose_name='phone')
    # photo = models.ImageField(blank=True, null=True, verbose_name='photo')
    photo = models.FilePathField(path=settings.MEDIA_ROOT / 'photo', null=True)
    is_bot = models.BooleanField(default=False, verbose_name='is bot')
    deleted = models.BooleanField(default=False, verbose_name='deleted')
    groups = models.ManyToManyField('TelegramChat', related_name='users')


class TelegramChat(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    username = models.CharField(max_length=255, null=True, blank=True, default='', verbose_name='username')
    photo = models.ImageField(blank=True, null=True, verbose_name='photo')
    title = models.CharField(max_length=255, null=True, blank=True, default='', verbose_name='title')
    participants = models.ManyToManyField(TelegramUser, related_name='chats', blank=True)


class TelegramMessage(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    from_user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE)
    from_chat = models.ForeignKey(TelegramChat, on_delete=models.CASCADE)
    message = models.TextField(db_index=True, null=True, default='', blank=True, verbose_name='message')
