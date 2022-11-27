import dataclasses
from typing import List, Optional, Union

from pandas import DataFrame

from code_challenge.api.graphql_data import GraphQLData
from code_challenge.api.graphql_query import GraphQLQuery
from code_challenge.api.graphql_reader import GraphQLReader
from code_challenge.models.company import Company
from code_challenge.models.price import Price, PriceUpdate
from code_challenge.models.recommendation import Recommendation
from code_challenge.services.recommendation_service import (
    RecommendationService,
)


class CompanyService:
    """Service to get company values from API"""

    def __init__(self, graphql_reader: GraphQLReader):
        self.graphql_reader = graphql_reader

    def get_companies(
        self, sector: Optional[str] = None, country: Optional[str] = None
    ) -> List[Company]:
        filter = {"sector": sector, "country": country}
        result = ["name", "ticker", "sector", "country"]
        query = GraphQLQuery.create_query("companies", filter, result)
        response = self.graphql_reader.query(query)
        return GraphQLData.convert_to_companies(response)

    @classmethod
    def get_ticker(cls, company: Union[Company, str]) -> str:
        if isinstance(company, Company):
            return company.ticker
        return company

    def get_prices(
        self,
        company: Union[Company, str],
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> DataFrame:
        ticker = self.get_ticker(company)
        filter = {
            "ticker": ticker,
            "startDate": start_date,
            "endDate": end_date,
        }
        result = ["date", "open", "high", "low", "close", "volume"]
        query = GraphQLQuery.create_query("prices", filter, result)
        response = self.graphql_reader.query(query)
        return GraphQLData.convert_to_data_frame(response)

    def get_recommendation(
        self,
        company: Union[Company, str],
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> DataFrame:
        ticker = self.get_ticker(company)
        filter = {
            "ticker": ticker,
            "startDate": start_date,
            "endDate": end_date,
        }
        result = ["date", "firm", "fromGrade", "toGrade"]
        query = GraphQLQuery.create_query("recommendations", filter, result)
        response = self.graphql_reader.query(query)
        df = GraphQLData.convert_to_data_frame(response)
        return RecommendationService().transform_scalar_to_average(df)

    def add_new_companies(self, companies: List[Company]) -> bool:
        for company in companies:
            data = dataclasses.asdict(company)
            result = ["name", "ticker", "sector", "country"]
            mutation = GraphQLQuery.create_mutation("addCompany", data, result)
            response = self.graphql_reader.query(mutation)
            GraphQLData.validate_response(response)
        return True

    def add_prices(
        self, company: Union[Company, str], prices: List[Price]
    ) -> bool:
        ticker = self.get_ticker(company)
        data_prices = [dataclasses.asdict(price) for price in prices]
        data = {"ticker": ticker, "prices": data_prices}
        result = ["status"]
        mutation = GraphQLQuery.create_mutation("addPrices", data, result)
        response = self.graphql_reader.query(mutation)
        GraphQLData.validate_response(response)
        return GraphQLData.verify_status(response)

    def add_single_price(
        self,
        company: Union[Company, str],
        date: str,
        open: float,
        high: float,
        low: float,
        close: float,
        volume: float,
    ) -> bool:
        prices = [Price(date, open, high, low, close, volume)]
        return self.add_prices(company, prices)

    def add_recommendations(
        self,
        company: Union[Company, str],
        recommendations: List[Recommendation],
    ) -> bool:
        ticker = self.get_ticker(company)
        data_rec = [dataclasses.asdict(r) for r in recommendations]
        data = {"ticker": ticker, "recommendations": data_rec}
        result = ["status"]
        mutation = GraphQLQuery.create_mutation(
            "addRecommendations", data, result
        )
        response = self.graphql_reader.query(mutation)
        GraphQLData.validate_response(response)
        return GraphQLData.verify_status(response)

    def add_single_recommendation(
        self,
        company: Union[Company, str],
        date: str,
        firm: str,
        fromGrade: str,
        toGrade: str,
    ) -> bool:
        recommendations = [Recommendation(date, firm, fromGrade, toGrade)]
        return self.add_recommendations(company, recommendations)

    def update_price(
        self,
        company: Union[Company, str],
        date: str,
        open: Optional[float] = None,
        high: Optional[float] = None,
        low: Optional[float] = None,
        close: Optional[float] = None,
        volume: Optional[float] = None,
    ) -> bool:
        ticker = self.get_ticker(company)
        price = dataclasses.asdict(
            PriceUpdate(date, open, high, low, close, volume)
        )
        data = {"ticker": ticker, "price": price}
        result = ["status"]
        mutation = GraphQLQuery.create_mutation("updatePrice", data, result)
        response = self.graphql_reader.query(mutation)
        GraphQLData.validate_response(response)
        return GraphQLData.verify_status(response)
