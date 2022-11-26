from typing import Optional

from code_challenge.api.graphql_reader import GraphQLReader
from code_challenge.api.graphql_data import GraphQLData
from code_challenge.api.graphql_query import GraphQLQuery


class CompanyService:
    """Service to get company values from API"""

    def __init__(self, graphql_reader: GraphQLReader):
        self.graphql_reader = graphql_reader

    def get_companies(
        self, sector: Optional[str] = None, country: Optional[str] = None
    ):
        filter = {"sector": sector, "country": country}
        result = ["name", "ticker", "sector", "country"]
        query = GraphQLQuery.create("companies", filter, result)
        response = self.graphql_reader.query(query)
        return GraphQLData.treat(response)
