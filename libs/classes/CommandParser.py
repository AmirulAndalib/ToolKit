import re
from calendar import isleap, monthrange
from datetime import datetime, timedelta
from typing import List, Optional

from aiogram import types
from asyncinit import asyncinit
from bot import bot, client
from libs.classes.Errors import ArgumentError, UserNotFound
from libs.src import system

from . import User, UserText, AdminPanel


def get_days_years(year: int, now: datetime):
    """
    Превращает года в дни
    """
    days = 0
    for y in range(now.year, now.year+year):
        year_days = 365
        if isleap(y):
            year_days += 1
        days += year_days
    return days


def get_days_month(month: int, now: datetime):
    """
    Превращает месяца в дни
    """
    days = 0
    years = month // 12
    month = month % 12

    for m in range(now.month, now.month + month):
        days += monthrange(now.year, m)[1]
    days += get_days_years(years, now)
    return days


@asyncinit
class AdminCommandParser:
    """
    Инструмент для парсинга команд
    """

    async def __init__(self, msg: types.Message, text: Optional[str] = None) -> None:
        self.src = UserText(msg.from_user.language_code)

        self.msg = msg
        self.chat = msg.chat
        self.owner: User = await User(user=msg.from_user)

        self.command = text if text else msg.text
        self.entities = msg.entities

        self.cmd: str = None
        self.action: str = None
        self.bot: str = None

        self.users: List[AdminPanel] = []

        self.now: datetime = datetime.now()
        self.until: datetime = self.now

        self.reason: str = ""

        await self.parse()
        await self.entities_parse()

        if not self.reason:
            self.reason = self.src.text.chat.admin.reason_empty
        if not (self.users or self.cmd or self.bot):
            raise ArgumentError(self.src.lang)

    async def parse(self):
        """
        Парс по regex
        """
        all = re.finditer(system.regex.parse.all, self.command)

        for match in all:
            group = match.lastgroup
            text: str = match.group(group)

            if group == "cmd":
                self.cmd = text
                self.bot = match.group("bot")
                self.action = match.group("action")

            elif group in ["id", "user"]:
                await self.to_user(text)
            elif group == "until":
                await self.to_date(match)
            elif group == "reason":
                self.reason += text

        delta = self.until - self.now
        if (delta.total_seconds() < 30 or delta.days > 366) and self.until.timestamp() != self.now.timestamp():
            await self.msg.answer(self.src.text.errors.UntilWaring)
            # self.until = self.now

    async def entities_parse(self):
        """
        Парс по message entities
        """
        for entity in self.entities:
            if entity.type == "text_mention":
                user = await AdminPanel(entity.user.id, self.owner)
                self.users.append(user)

    async def to_user(self, auth: str) -> User:
        """
        Преобразует упоминание в User
        """
        user = await AdminPanel(auth, self.owner)
        try:
            pass
        except Exception as e:
            raise UserNotFound(self.msg.from_user.language_code)
        self.users.append(user)

    async def to_date(self, match: re.Match) -> int:
        """
        Преобразует строку в datetime
        """
        num: int = int(match.group("num"))
        datetype: str = match.group("type")

        if datetype == "s":
            delta = timedelta(seconds=num)
        elif datetype == "m":
            delta = timedelta(minutes=num)
        elif datetype == "h":
            delta = timedelta(hours=num)
        elif datetype == "d":
            delta = timedelta(days=num)
        elif datetype == "M":
            delta = timedelta(days=get_days_month(num, self.now))
        elif datetype == "y":
            delta = timedelta(days=get_days_years(num, self.now))

        self.until += + delta

    async def undo(self) -> str:
        if self.action.startswith("un"):
            return self.action.removeprefix("un")
        else:
            return "un" + self.action

    @property
    def format_until(self):
        """
        Возвращает форматированую дату
        """
        if self.now == self.until:
            return self.src.text.chat.admin.forever
        return f"{self.until.year}-{self.until.month}-{self.until.day}"

    @property
    def format_users(self):
        """
        Возвращает форматированных пользователей 
        """
        result = ""
        for user in self.users:
            result += f"{user.link},"
        return result.removesuffix(",")