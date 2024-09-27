from __future__ import annotations
from typing import Protocol, TYPE_CHECKING

if TYPE_CHECKING:
    from bot.DTO import CurrencyDTO


class AdapterProtocol(Protocol):
    async def get_currency_rate(self, currency: str) -> CurrencyDTO:
        pass
