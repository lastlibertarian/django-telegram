from pyrogram import Client
import configparser
import os
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoTelegram.settings")
config = configparser.ConfigParser()
config_file_path = '%s/config.ini' % settings.BASE_DIR
config.read(config_file_path)

api_id = config.get('tgClient', 'api_id')
api_hash = config.get('tgClient', 'api_hash')
username = config.get('tgClient', 'username')

pyrobot = Client(name=f'pyrogram_{username}', api_id=api_id, api_hash=api_hash)


def login():
    with pyrobot:
        pyrobot.send_message("me", "**Pyrogram**")
