import logging
from typing import Dict

import yfinance as yf

from code_challenge.api.graphql_reader import GraphQLReader
from code_challenge.exceptions.code_challenge_exception import \
    CodeChallengeException
from code_challenge.models.company import Company
from code_challenge.models.price import Price
from code_challenge.models.recommendation import Recommendation
from code_challenge.services.company_service import CompanyService


class FeedY:
    """Feed for Y!Finance"""

    def __init__(self, graphql_reader: GraphQLReader):
        self.graphql_reader = graphql_reader

    def fill(self, ticker: str):
        service = CompanyService(self.graphql_reader)

        logging.info("Reading from Y!Finance")

        company = yf.Ticker(ticker)
        info: Dict = company.info or {}
        history = company.history(period="max")
        recs = company.recommendations

        logging.info("Adding data")

        try:
            companies = [
                Company(
                    name=info["longName"],
                    ticker=ticker,
                    sector=info["sector"],
                    country=info["country"],
                )
            ]
            service.add_new_companies(companies)
            logging.info(f"Added company: {ticker}")

            prices = [
                Price(
                    date=index.strftime("%Y-%m-%d"),
                    open=row["Open"],
                    high=row["High"],
                    low=row["Low"],
                    close=row["Close"],
                    volume=row["Volume"],
                )
                for index, row in history.iterrows()
            ]
            service.add_prices(ticker, prices)
            logging.info(f"Added prices: {len(prices)}")

            recommendations = [
                Recommendation(
                    date=index.strftime("%Y-%m-%d"),  # type: ignore
                    firm=row["Firm"],
                    fromGrade=row["From Grade"],
                    toGrade=row["To Grade"],
                )
                for index, row in recs.iterrows()  # type: ignore
            ]
            service.add_recommendations(ticker, recommendations)
            logging.info(f"Added recommendations: {len(recommendations)}")

        except CodeChallengeException as e:
            print(str(e))
