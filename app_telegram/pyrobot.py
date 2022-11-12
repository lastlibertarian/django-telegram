from pyrogram import Client
import configparser
import os
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoTelegram.settings")


print(settings.BASE_DIR)
