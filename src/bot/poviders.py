from __future__ import annotations
from typing import TYPE_CHECKING
from bot.interfaces import AdapterProtocol
from bot.api_adapters import CbrDailyAdapter

if TYPE_CHECKING:
    from aiohttp import ClientSession


def provide_api(api_url: str, session: ClientSession) -> AdapterProtocol:
    if api_url == "https://www.cbr-xml-daily.ru":
        return CbrDailyAdapter(session=session)
    else:
        raise ValueError("Unsupported API.")
