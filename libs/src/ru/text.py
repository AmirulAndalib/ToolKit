from aiogram.utils.markdown import hlink as l

cancel = "\n/cancel - отмена"


class errors:
    until = "Если пользователь заблокирован на срок более 366 дней или менее 30 секунд с текущего времени, он считается заблокированным навсегда."
    UntilWaring = f"❗ {until}"

    CommandNotFound = "⚠ Команда не найдена"
    UserNotFound = "⚠ Пользователь не найден"
    ArgumentError = "⚠ Неверный аргумент"
    HasNotPermission = "⚠ У вас нет прав"
    EmptyOwns = "⚠ Ты не владеешь чатами"
    TypeError = "⚠ Не тот тип"
    AlreadyExists = "⚠ Уже существует"
    NotReply = "⚠ Нет ответа"
    BotHasNotPermission = "⚠ У бота нет прав или их не достаточно"


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
                    "┣ /ban /unban ⛔ \n" +\
                    "┣ /mute /unmute ⚠ \n" +\
                    "┗ /kick 🔇"
    restrict_admin = "У бота <b>забрали</b> права администратора \n" +\
                     "Теперь вы <b>НЕ можете</b> использовать такие команды, как \n" +\
                     "┣ /ban /unban ⛔ \n" +\
                     "┣ /mute /unmute ⚠ \n" +\
                     "┗ /kick 🔇"

    class admin:
        reason = "Причина - {reason} \n"
        admin = "Администратор - {admin} \n"
        until = "До - {until} \n"

        unmute = "{users} размучен \n" + reason + admin
        multi_unmute = "{users} размучены \n" + reason + admin

        mute = "{users} замучен \n" + reason + admin + until
        multi_mute = "{users} замучены \n" + reason + admin + until

        kick = "{users} исключён \n" + reason + admin
        multi_kick = "{users} исключёны \n" + reason + admin

        unban = "{users} разаблокирован \n" + reason + admin
        multi_unban = "{users} разаблокированы \n" + reason + admin

        ban = "{users} заблокирован \n" + reason + admin + until
        multi_ban = "{users} заблокированы \n" + reason + admin + until

        forever = "31 Февраля 1970 года"
        reason_empty = "Без причины"


class help:
    users = f"\nУпоминания (@username,{l('Вася Пупкин','t.me/username')})"
    until = "\nДата[s|m|h|d|M|y] (1m 30s,1M)"
    reason = "\n\"Причина\" (Да прям в кавычках)"

    ban = "/ban" + users + until + reason
    unban = "/unban" + users + reason
    kick = "/kick" + users + reason
    mute = "/mute" + users + until + reason
    unmute = "/unmute" + users + reason
