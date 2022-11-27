from dataclasses import dataclass


@dataclass
class Recommendation:
    """Recommendation model"""

    date: str
    firm: float
    fromGrade: float
    toGrade: float
