import argparse

from tabulate import tabulate

from code_challenge.api.config_file import ConfigFile
from code_challenge.api.graphql_reader import GraphQLReader
from code_challenge.services.company_service import CompanyService
from code_challenge.exceptions.code_challenge_exception import CodeChallengeException


def main():
    parser = argparse.ArgumentParser("code_challenge")
    command = parser.add_subparsers(dest="command")
    command.required = True
    get_companies = command.add_parser("get_companies")
    get_companies.add_argument("-s", "--sector")
    get_companies.add_argument("-c", "--country")
    get_prices = command.add_parser("get_prices")
    get_prices.add_argument("ticker")
    get_prices.add_argument("-s", "--start_date")
    get_prices.add_argument("-e", "--end_date")
    get_recommendations = command.add_parser("get_recommendations")
    get_recommendations.add_argument("ticker")
    get_recommendations.add_argument("-s", "--start_date")
    get_recommendations.add_argument("-e", "--end_date")
    args = parser.parse_args()

    settings = ConfigFile().read()
    reader = GraphQLReader(settings)
    service = CompanyService(reader)

    try:
        if args.command == "get_companies":
            sector = args.sector
            country = args.country
            df = service.get_companies_as_dataframe(sector, country)
            show(df)

        if args.command == "get_prices":
            ticker = args.ticker
            start_date = args.start_date
            end_date = args.end_date
            df = service.get_prices(ticker, start_date, end_date)
            show(df)

        if args.command == "get_recommendations":
            ticker = args.ticker
            start_date = args.start_date
            end_date = args.end_date
            df = service.get_recommendation(ticker, start_date, end_date)
            show(df)
    except (CodeChallengeException) as e:
        print(str(e))


def show(dataframe):
    print(tabulate(dataframe, headers="keys", tablefmt="psql"))
