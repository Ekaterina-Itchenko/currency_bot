from __future__ import annotations
import json
from typing import TYPE_CHECKING

from bot.DTO import CurrencyDTO
from bot.errors import CurrencyNotFoundError
from bot.interfaces import AdapterProtocol
from config import API_URL

if TYPE_CHECKING:
    from aiohttp import ClientSession


class CbrDailyAdapter(AdapterProtocol):
    def __init__(self, session: ClientSession) -> None:
        self._session = session

    async def get_currency_rate(self, currency: str) -> CurrencyDTO:
        try:
            async with self._session.get(
                url=(API_URL + "/daily_json.js")
            ) as response:
                all_currencies = json.loads(await response.text())
                res = CurrencyDTO(
                    rate=all_currencies['Valute'][currency]['Value']
                )
                return res
        except KeyError:
            raise CurrencyNotFoundError(
                f'The currenccy "{currency}" has not found.'
            )
