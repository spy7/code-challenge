import requests

from code_challenge.api.settings import Settings


class GraphQLReader:
    """Helper to read data from GraphQL"""

    def __init__(self, settings: Settings):
        self.settings = settings

    def get_headers(self) -> dict:
        return {"Authorization": f"Bearer {self.settings.token}"}

    def query(self, query: str) -> dict:
        response = requests.post(
            f"{self.settings.host}/{self.settings.endpoint}",
            json={"query": query},
            headers=self.get_headers(),
        )
        return response.json()
