import config
from aiogram.types import InlineKeyboardMarkup as IM
from src import system
from libs.buttons import Button, Menu, Submenu
from libs.settings import Elements, Property, Settings
from libs.locales import Text as _

statistic_title = _("Off - Nothing will be saved (nothing) \n" +
                    "Date only - Date of message will be saved (date) \n" +
                    "Full - Text and data of message will be saved (text and data) \n" +
                    "Current: {mode}")
_statistic_property = Property(
    statistic_title,
    _("Statistic settings"),
    "statistic", row_width=3
).add(
    Button(_("Off"), "statistic:0"),
    Button(_("Date only"), "statistic:1"),
    Button(_("Full"), "statistic:2")
)


class chat:
    @staticmethod
    def start_button(chat_id) -> Button:
        return Button(_("Chat settings (owner only)"),
                      url=f"t.me/{config.bot.username}?start=chatsettings_{chat_id}").menu

    class admin:
        undo = Button(_("↩ Undo"), "undo")

        check_poll = Button(_("✅ Check poll"), "check_poll")
        cancel_poll = Button(_("⛔ Cancel poll"), "cancel_poll")

        poll = IM(row_width=1).add(
            check_poll,
            cancel_poll
        )


class private:
    class settings:
        chat_settings = Button(_("Chats"), "chat_settings")
        private_settings = Button(_("Self"), "private_settings")
        settings = Menu(_("Choose what you want to customize"), row_width=2).add(
            chat_settings,
            private_settings
        )

        chat_list = Menu(_("Choose chat"), undo=True)

        class chat:
            add_alias = Button(_("Add alias"), "add_alias")

            settings = Settings(_("Choose what you want to customize"), row_width=2, undo=True).add(
                Property(_("Alias for sticker") + "\n" + _("Click to delete"), _("Alias for sticker"),
                         "sticker_alias", row_width=1).add(
                    add_alias,
                    Elements("{v}", "delete_alias:{k}")
                ),
                Property(_("Alias for text") + "\n" + _("Click to delete"), _("Alias for text"),
                         "text_alias", row_width=1).add(
                    add_alias,
                    Elements("{k} → {v}", "delete_alias:{k}")
                ),
                _statistic_property

            )

            delete = Menu(_("Delete ?"), hide=True)
            delete_yes = Button(_("Yes 🗑"), "delete_yes")
            delete_no = Button(_("No ↩"), "back")
            delete.add(
                delete_yes,
                delete_no
            )

        class private:
            change_lang = Submenu(_("Choose language"), _("Change language"), "change_lang", row_width=4).add(
                *[Button(t, f"change_lang:{d}")
                  for d, t in system.langs.items()],
                Button("🇬🇧 English", "change_lang:other")
            )

            settings = Settings(_("Choose what you want to customize"), undo=True).add(
                change_lang,
                _statistic_property
            )


back = Button(_("↩ Back"), "back")
delete_this = Button(_("🗑 Delete"), "delete_this")
