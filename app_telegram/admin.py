from django.contrib import admin
from app_telegram.models import TelegramChat, TelegramUser


class TelegramChatAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']


class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']


admin.site.register(TelegramChat, TelegramChatAdmin)
admin.site.register(TelegramUser, TelegramUserAdmin)
