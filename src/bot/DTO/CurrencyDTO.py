from dataclasses import dataclass
from typing import Optional


@dataclass
class CurrencyDTO:
    rate: Optional[float]
