from dataclasses import dataclass


@dataclass
class Price:
    """Price model"""

    date: str
    open: float
    high: float
    low: float
    close: float
    volume: float
