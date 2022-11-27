from dataclasses import dataclass


@dataclass
class Recommendation:
    """Recommendation model"""

    date: str
    firm: str
    fromGrade: str
    toGrade: str
