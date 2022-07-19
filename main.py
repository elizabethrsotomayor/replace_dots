import re


def replace_dots(string: str) -> str:
    return re.sub(r"\.", "-", string)
