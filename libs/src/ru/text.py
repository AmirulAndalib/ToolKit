from aiogram.utils.markdown import hbold as b
from aiogram.utils.markdown import hcode as c
from aiogram.utils.markdown import hitalic as i
from aiogram.utils.markdown import hlink as l
from aiogram.utils.markdown import text as t

cancel = "\n/cancel - отмена"


class errors:
    class restrict:
        pass

    class argument_error:
        ArgumentError = "⚠ Неверный аргумент"

        incorrect = f'Аргумент "{b("{arg_name}")}" неверен'
        required = f'Аргумент "{b("{arg_name}")}" обязателен'

    until = "Если пользователь заблокирован на срок более 366 дней или менее 30 секунд с текущего времени, он считается заблокированным навсегда."
    UntilWaring = f"❗ {until}"

    CommandNotFound = "⚠ Команда не найдена"
    UserNotFound = "⚠ Пользователь не найден"
    HasNotPermission = "⚠ У вас недостаточно прав"
    EmptyOwns = "⚠ Ты не владеешь чатами"
    TypeError = "⚠ Не тот тип"
    AlreadyExists = "⚠ Уже существует"
    NotReply = "⚠ Нет ответа"
    BotHasNotPermission = "⚠ У бота нет прав или их не достаточно"
    BackError = "⚠ Ошибка возврата"
    PollCheck = "⚠ Недостаточно голосов"


class private:
    start_text = "Привет я ToolKit бот и я предназначен для всего что можно представить 😜 \n" +\
                 "Вот в вкратце что я умею 😊 \n" +\
                 "┣ Редактировать фото 🌅 \n" +\
                 "┣ Администрировать группы ⚙️ \n" +\
                 "┣ Расшифровывать ГС 🎤 \n" +\
                 "┣ Генерировать ГС 🎙 \n" +\
                 "┗ Генерировать мемы 😎"

    class settings:
        chat_loading = "🕒 Подождите, чаты загружаются"
        sticker = "1⃣ Пришли мне стикер" + cancel
        text = "1⃣ Пришли мне текст" + cancel

        command = "2⃣ Пришли мне команду"


class chat:
    _perm = "┣ /ban /unban ⛔ \n" +\
            "┣ /mute /unmute 🔇 \n" +\
            "┣ /purge 🗑\n" +\
            "┗ /kick ⚠"

    start_text = "Привет, я ToolKit бот \n" +\
                 "Вот что я могу делать в этом чате \n" +\
                 "┣ Администрировать ⚙️ \n" +\
                 "┗ Расшифровывать ГС 🎤 \n" +\
                 " \n" +\
                 "Чтобы команды для администрирования работали, пожалуйста предоставьте эти права\n" +\
                 "┣ Удаление сообщений ⚠ \n" +\
                 "┣ Создавать ссылки 🔗 \n" +\
                 "┗ Банить пользователей ⛔"
    promote_admin = "У бота <b>появились</b> права администратора \n" +\
                    "Теперь вы <b>можете</b> использовать такие команды, как \n" +\
                    _perm
    restrict_admin = "У бота <b>забрали</b> права администратора \n" +\
                     "Теперь вы <b>НЕ можете</b> использовать такие команды, как \n" +\
                     _perm

    class admin:
        reason = f"Причина ❓ - {c('{reason}')} \n"
        admin = f"Администратор 👤 - {i('{admin}')} \n"
        until = f"До ⌛ - {b('{until}')} \n"

        unmute = "{user} размучен 🔈 \n" + reason + admin
        multi_unmute = "{user} размучены 🔈 \n" + reason + admin
        unmute_poll = "🔈 Размутить - {user} ?"

        mute = "{user} замучен 🔇 \n" + reason + admin + until
        multi_mute = "{user} замучены 🔇 \n" + reason + admin + until
        mute_poll = "🔇 Замутить - {user} ?"

        kick = "{user} исключён ⚠ \n" + reason + admin
        multi_kick = "{user} исключёны ⚠ \n" + reason + admin
        kick_poll = "⚠ Исключить - {user} ?"

        unban = "{user} разаблокирован ✅ \n" + reason + admin
        multi_unban = "{user} разаблокированы ✅ \n" + reason + admin
        unban_poll = "✅ Разблокировать - {user} ?"

        ban = "{user} заблокирован ⛔ \n" + reason + admin + until
        multi_ban = "{user} заблокированы ⛔ \n" + reason + admin + until
        ban_poll = "⛔ Заблокировать - {user} ?"

        options_poll = ["✅ Да", "⛔ Нет"]

        forever = "31 Февраля 1970 года"
        reason_empty = "Без причины"

        purge = "🗑 В чате удалено {count} сообщений"


class help:
    users = f'👥 Упоминания (@username,{l("Вася Пупкин","t.me/username")} или ответ) \n'
    until = '⏳ Дата[s|m|h|d|M|y] (1m 30s или 1M) \n'
    reason = '❔ "Причина" (Да прям в кавычках) \n'
    poll = '📈 Сделать опрос (-p --poll)'

    ban = "⛔ /ban \n" + users + until + reason + poll
    unban = "✅ /unban \n" + users + reason + poll
    kick = "⚠ /kick \n" + users + reason + poll
    mute = "🔇 /mute \n" + users + until + reason + poll
    unmute = "🔈 /unmute \n" + users + reason + poll

    count = "\n🔢 Количество (2 - 1000)"
    reply = "\n⤴ Ответьте для удаления выше"

    purge = "🗑 /purge" + count + reply
