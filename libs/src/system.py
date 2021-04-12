import re


class regex:
    class parse:
        cmd = r"(?P<cmd>^/(?P<action>[0-9a-zA-Z_]+)(?P<bot>@[0-9a-zA-Z_]+)?)"
        until = r"(?P<until>(?P<num>[1-9][0-9]*)(?P<type>[s|m|h|d|M|y]))"
        user = r"(?P<user>@[a-zA-Z][a-zA-Z0-9_]{4,})|(?P<id>[1-9][0-9]*)"
        reason = r"(?P<reason>[\w][\w ]+[\w])"
        all = re.compile(f"{cmd}|{until}|{user}|{reason}")


if __name__ == "__main__":
    print(regex.parse.all.pattern)
