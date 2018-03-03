from typing import Any
from pydu.compat import text_type


def safeunicode(obj: Any, encoding: str) -> text_type: ...
def safeencode(obj: Any, encoding: str) -> bytes: ...
def _strips(direction: str, text: str, remove: str) -> str: ...
def rstrips(text: str, remove: str) -> str: ...
def lstrips(text: str, remove: str) -> str: ...
def strips(text: str, remove: str) -> str: ...
def common_prefix(l: list) -> str: ...
def common_suffix(l: list) -> str: ...
def sort(s: str, reverse: bool) -> str: ...
