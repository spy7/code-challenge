import json

import pandas as pd

from code_challenge.exceptions.code_challenge_exception import \
    CodeChallengeException


class GraphQLData:
    """Helper to treat result data and convert to data frame"""

    @classmethod
    def treat(cls, response: str) -> pd.DataFrame:
        data = json.loads(response)
        if "errors" in data:
            message = "\n".join([e["message"] for e in data["errors"]])
            raise CodeChallengeException(message)
        return pd.json_normalize(list(data["data"].values())[0])
