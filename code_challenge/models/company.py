from dataclasses import dataclass


@dataclass
class Company:
    """Company model"""

    name: str
    ticker: str
    sector: str
    country: str
