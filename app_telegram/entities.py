from telethon.sync import TelegramClient
from app_telegram.models import TelegramChat, TelegramUser, TelegramMessage
import asyncio
from django.core.files import File
from django.conf import settings
import urllib
import logging
from urllib import request

logger = logging.getLogger(__name__)
import os

api_id = 12359630
api_hash = 'f85fd0ec567c2f9ed2378fc4bc59a137'


class Parser:

    def get_chat(self, chat_username: str) -> bool:
        """Getting and saving chat info"""
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        userbot = TelegramClient("lastbart1", api_id, api_hash, loop=loop)
        with userbot:
            # telegram_chat = userbot.get_entity(chat_username)
            # if telegram_chat.photo:
            #     photo_path = userbot.download_profile_photo(chat_username,
            #                                                 file=f'media/photos/{telegram_chat.id}',
            #                                                 download_big=False)
            # chat = TelegramChat.objects.get_or_create(id=telegram_chat.id,
            #                                           username=telegram_chat.username,
            #                                           title=telegram_chat.title,
            #                                           photo=str(photo_path) if photo_path else None)
            # chat.save()

            users = userbot.iter_participants(chat_username)
            for i_user in users:
                if i_user.photo:
                    userbot.download_profile_photo(i_user.id,
                                                   file=f'{settings.MEDIA_ROOT}/photo/{i_user.id}',
                                                   download_big=False)

                user: TelegramUser = TelegramUser.objects.get_or_create(id=i_user.id,
                                                                        username=i_user.username,
                                                                        first_name=i_user.first_name,
                                                                        last_name=i_user.last_name,
                                                                        phone=i_user.phone,
                                                                        is_bot=i_user.bot,
                                                                        deleted=i_user.deleted,
                                                                        photo=f'{i_user.id}.jpg' if i_user.photo else None)

                # result = request.urlretrieve(user_photo_path)
                # print(os.path.basename(user_photo_path))
                # print(result)
                # with open(user_photo_path, 'rb') as file:
                #     user[0].photo.save(f'{i_user.id}.jpg', file)

    # def get_users(self, chat_username: str) -> bool:
    #     loop = asyncio.new_event_loop()
    #     asyncio.set_event_loop(loop)
    #     userbot = TelegramClient("lastbart1", api_id, api_hash, loop=loop)
    #     chat = TelegramChat.objects.filter(username=chat_username).first()
    #     # logger.info(chat)
    #     with userbot:
    #         if not chat:
    #             self.get_chat(chat_username)
    #             return self.get_users(chat_username)
    #         users = userbot.get_participants(chat_username, limit=1)
    #         logger.info(users)
    #         for i_user in users:
    #             if i_user.photo:
    #                 photo_path = userbot.download_profile_photo(chat_username,
    #                                                             file=f'media/photos/{i_user.id}',
    #                                                             download_big=False)
    #             user = TelegramUser.objects.create(id=i_user.id,
    #                                                username=i_user.username,
    #                                                first_name=i_user.first_name,
    #                                                last_name=i_user.last_name,
    #                                                phone=i_user.phone,
    #                                                is_bot=i_user.bot,
    #                                                deleted=i_user.deleted,
    #                                                photo=str(photo_path) if photo_path else None)
    #             user.save()

# User(id=498029296, is_self=False, contact=False, mutual_contact=False, deleted=False, bot=False, bot_chat_history=False,
#      bot_nochats=False, verified=False, restricted=False, min=False, bot_inline_geo=False, support=False, scam=False,
#      apply_min_photo=True, fake=False, bot_attach_menu=False, premium=False, attach_menu_enabled=False,
#      access_hash=-148684264632462621, first_name='Igor', last_name='Balobanov', username='IgorBaloo',
#      phone='79062589618', photo=None, status=UserStatusRecently(), bot_info_version=None, restriction_reason=[],
#      bot_inline_placeholder=None, lang_code=None)
