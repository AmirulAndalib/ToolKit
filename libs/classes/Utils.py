import re
from time import time
from typing import Dict, Text, Tuple, Union

import config as c
from aiogram import types as t
from aiogram.dispatcher import filters as f
from bot import bot
from libs.objects import Database

from . import Chat, User, UserText


async def get_help(msg: t.Message):
    """
    Отправка help текста нужной локализации
    """
    if msg.get_command() == msg.text:
        command = msg.get_command(True)
        src = UserText(msg.from_user.language_code)

        try:
            text = getattr(src.text.help, command)
            await msg.reply(text, disable_web_page_preview=True)
            return False
        except:
            pass
    return True


async def mark_write(msg: t.Message):
    await msg.answer_chat_action(t.ChatActions.TYPING)
    return True

is_chat = f.ChatTypeFilter((t.ChatType.GROUP, t.ChatType.SUPERGROUP))
is_private = f.ChatTypeFilter((t.ChatType.PRIVATE))
is_reply = f.IsReplyFilter(True)


def bot_has_permission(*permissions):
    permissions = list(permissions)

    async def filter(msg: t.Message):
        member = await bot.get_chat_member(msg.chat.id, c.bot.id)
        for permission in permissions:
            can = getattr(member, permission)
            if not can:
                return False
        return True
    return filter


def add_member(upd: t.ChatMemberUpdated):
    old = upd.old_chat_member
    new = upd.new_chat_member
    return not old.is_chat_member() and new.is_chat_member()


def removed_member(upd: t.ChatMemberUpdated):
    old = upd.old_chat_member
    new = upd.new_chat_member
    return old.is_chat_member() and not new.is_chat_member()


def promote_admin(upd: t.ChatMemberUpdated):
    old = upd.old_chat_member
    new = upd.new_chat_member
    return not old.is_chat_admin() and new.is_chat_admin()


def restrict_admin(upd: t.ChatMemberUpdated):
    old = upd.old_chat_member
    new = upd.new_chat_member
    return old.is_chat_admin() and not new.is_chat_admin()


def clb(data):
    pattern = re.compile(data)

    async def filter(clb: t.CallbackQuery):
        if pattern.match(clb.data):
            return True
        return False
    return filter


async def alias(msg: t.Message, handler=True) -> Union[bool, str]:
    chat: Chat = await Chat(chat=msg.chat)
    if msg.sticker:
        text = msg.sticker.file_unique_id
        aliases = chat.sticker_aliases
    elif msg.text:
        text = msg.text
        aliases = chat.command_aliases

    if handler:
        return text in aliases
    else:
        return aliases[text]


async def chek(msg: t.Message):
    if await is_chat.check(msg):
        await Chat(chat=msg.chat)
    if not Database.get_user(msg.from_user.id):
        await User(user=msg.from_user)

    return False
