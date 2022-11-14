from django.shortcuts import render
from telethon.sync import TelegramClient
from app_telegram.models import TelegramChat, TelegramUser, TelegramMessage
import asyncio
from django.views import generic
from app_telegram.entities import Parser
from django import views


def thanks(request):
    parser = Parser()
    parser.get_chat('blackmastchat')
    m = TelegramChat.objects.first()
    return render(request, 'index.html', {'me': m})


class UserList(generic.ListView):
    model = TelegramUser
    template_name = 'user_list.html'
    context_object_name = 'user_list'
    paginate_by = 50


# class UserList(views.View):
#
#     def get(self, request):
#         user_list = TelegramUser.objects.all()
#         return render(request, 'user_list.html', {'user_list': user_list})












# Channel(id=1464357134,
#         title='♣️ 𝔹𝕝𝕒𝕔𝕜𝕄𝔸𝕊𝕋ℂ𝕙𝕒𝕥',
#         photo=ChatPhoto(photo_id=5411121089280588533,
#                         dc_id=2,
#                         has_video=True,
#                         stripped_thumb=b'\x01\x08\x08HW/ $\x1c`\x8a(\xa2\xb0\x96\xe7\\z\x9f'),
#         date=datetime.datetime(2021, 11, 7, 18, 9, 45, tzinfo=datetime.timezone.utc),
#         creator=False,
#         left=False,
#         broadcast=False,
#         verified=False,
#         megagroup=True,
#         restricted=False,
#         signatures=False,
#         min=False,
#         scam=False,
#         has_link=False,
#         has_geo=False,
#         slowmode_enabled=False,
#         call_active=False,
#         call_not_empty=False,
#         fake=False,
#         gigagroup=False,
#         noforwards=False,
#         join_to_send=False,
#         join_request=False,
#         access_hash=-3567731927928292715,
#         username='BlackMASTChat',
#         restriction_reason=[],
#         admin_rights=ChatAdminRights(change_info=True,
#                                      post_messages=False,
#                                      edit_messages=False,
#                                      delete_messages=True,
#                                      ban_users=True,
#                                      invite_users=True,
#                                      pin_messages=True,
#                                      add_admins=True,
#                                      anonymous=False,
#                                      manage_call=True,
#                                      other=True),
#         banned_rights=None,
#         default_banned_rights=ChatBannedRights(
#             until_date=datetime.datetime(2038, 1, 19, 3, 14, 7, tzinfo=datetime.timezone.utc),
#             view_messages=False,
#             send_messages=False,
#             send_media=False,
#             send_stickers=False,
#             send_gifs=False,
#             send_games=False,
#             send_inline=False,
#             embed_links=False,
#             send_polls=False,
#             change_info=True,
#             invite_users=False,
#             pin_messages=True),
#         participants_count=None)
# return
# [Message(id=60597, peer_id=PeerChannel(channel_id=1464357134),
#          date=datetime.datetime(2022, 11, 13, 17, 1, 6, tzinfo=datetime.timezone.utc), message='', out=False,
#          mentioned=False, media_unread=False, silent=False, post=False, from_scheduled=False, legacy=False,
#          edit_hide=False, pinned=False, noforwards=False, from_id=PeerUser(user_id=1464831406), fwd_from=None,
#          via_bot_id=None, reply_to=None, media=MessageMediaDocument(nopremium=False,
#                                                                     document=Document(id=5442792139010351150,
#                                                                                       access_hash=-3951519124211304124,
#                                                                                       file_reference=b'\x02WHQ\x0e\x00\x00\xec\xb5cq6t\x1f\xc1\xe3RL\x82\xcd\xc3\xd8\x18\x96\xc5S,BV',
#                                                                                       date=datetime.datetime(2022, 11,
#                                                                                                              13, 13, 27,
#                                                                                                              29,
#                                                                                                              tzinfo=datetime.timezone.utc),
#                                                                                       mime_type='video/mp4',
#                                                                                       size=5959458, dc_id=2,
#                                                                                       attributes=[
#                                                                                           DocumentAttributeVideo(
#                                                                                               duration=41, w=464, h=848,
#                                                                                               round_message=False,
#                                                                                               supports_streaming=True),
#                                                                                           DocumentAttributeFilename(
#                                                                                               file_name='IMG_7176.MP4')],
#                                                                                       thumbs=[
#                                                                                           PhotoStrippedSize(type='i',
#                                                                                                             bytes=b"\x01(\x16\xcbh\xd1\x7f\x88\xd4G\x15.7\x86\xf5\xa8\xa8\x18\xf4@\xd9\xe6\x8aT\xe0Q@\x0e@v\xe5z\x9ac\xc6\xe3\x92(F\xc1\xc5?\xcbf?{\x8a\x00\x8c\x0f|QO\xf2\xc8=sE\x001\x08\x0e\x0b\x0e+b\xf8\xc0\xb6\xd2\x14\xfb1\xfe\xef\x97\x8d\xddE\x14P#'\xcd\xf6\xa2\x8a(\x19"),
#                                                                                           PhotoSize(type='m', w=175,
#                                                                                                     h=320, size=4703)],
#                                                                                       video_thumbs=[]),
#                                                                     ttl_seconds=None), reply_markup=None, entities=[],
#          views=None, forwards=None,
#          replies=MessageReplies(replies=0, replies_pts=82837, comments=False, recent_repliers=[], channel_id=None,
#                                 max_id=None, read_max_id=None), edit_date=None, post_author=None, grouped_id=None,
#          reactions=None, restriction_reason=[], ttl_period=None), total = 41504]


#

# User(id=498029296, is_self=False, contact=False, mutual_contact=False, deleted=False, bot=False, bot_chat_history=False,
#      bot_nochats=False, verified=False, restricted=False, min=False, bot_inline_geo=False, support=False, scam=False,
#      apply_min_photo=True, fake=False, bot_attach_menu=False, premium=False, attach_menu_enabled=False,
#      access_hash=-148684264632462621, first_name='Igor', last_name='Balobanov', username='IgorBaloo',
#      phone='79062589618', photo=None, status=UserStatusRecently(), bot_info_version=None, restriction_reason=[],
#      bot_inline_placeholder=None, lang_code=None)
