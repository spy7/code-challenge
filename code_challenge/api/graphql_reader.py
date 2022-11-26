import json

import requests

from code_challenge.api.config_file import ConfigFile


class GraphQLReader:
    """Helper to read data from GraphQL"""

    def __init__(self, settings=None):
        if not settings:
            settings = ConfigFile().read()
        self.settings = settings

    def get_headers(self) -> dict:
        return {"Authorization": f"Bearer {self.settings.token}"}

    def query(self, query: str) -> str:
        response = requests.post(
            f"{self.settings.host}/{self.settings.endpoint}",
            json={"query": query},
            headers=self.get_headers(),
        )
        return response.text

    def mutation(self, mutation: str) -> dict:
        response = requests.post(
            f"{self.settings.host}/{self.settings.endpoint}",
            json={"mutation": mutation},
            headers=self.get_headers(),
        )
        return json.loads(response.text)
