from typing import Dict, List

from pandas import DataFrame, json_normalize

from code_challenge.exceptions.code_challenge_exception import (
    CodeChallengeException,
)
from code_challenge.models.company import Company


class GraphQLData:
    """Helper to treat result data and convert them"""

    @classmethod
    def validate_response(cls, response: Dict) -> None:
        if "errors" in response:
            message = "\n".join([e["message"] for e in response["errors"]])
            raise CodeChallengeException(message)

    @classmethod
    def verify_status(cls, response: Dict) -> bool:
        return list(response["data"].values())[0]["status"] == "OK"

    @classmethod
    def extract_data(cls, response: Dict) -> List:
        return list(response["data"].values())[0]

    @classmethod
    def convert_to_data_frame(cls, response: Dict) -> DataFrame:
        cls.validate_response(response)
        data = cls.extract_data(response)
        return json_normalize(data)

    @classmethod
    def convert_to_companies(cls, response: Dict) -> List[Company]:
        cls.validate_response(response)
        data = cls.extract_data(response)
        return [
            Company(
                name=d["name"],
                ticker=d["ticker"],
                sector=d["sector"],
                country=d["country"],
            )
            for d in data
        ]
