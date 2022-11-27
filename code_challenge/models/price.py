from dataclasses import dataclass
from typing import Optional


@dataclass
class Price:
    """Price model to insert"""

    date: str
    open: float
    high: float
    low: float
    close: float
    volume: float


@dataclass
class PriceUpdate:
    """Price model to update"""

    date: str
    open: Optional[float]
    high: Optional[float]
    low: Optional[float]
    close: Optional[float]
    volume: Optional[float]
