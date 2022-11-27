from code_challenge.api.graphql_reader import GraphQLReader
# from code_challenge.models.company import Company
from code_challenge.models.price import Price
from code_challenge.services.company_service import CompanyService
from code_challenge.api.config_file import ConfigFile


def main(*args, **kwargs):
    settings = ConfigFile().read()
    reader = GraphQLReader(settings)
    service = CompanyService(reader)
    # print(service.get_companies())
    # print(service.get_prices("AAPL"))
    # print(service.get_recommendation("AAPL"))
    # companies = [Company(name="ab", ticker="AB", sector="t", country="PT")]
    # print(service.add_new_companies(companies))
    prices = [
        Price(date="2022-11-13", open=2, high=3, low=2, close=2.5, volume=10)
    ]
    print(service.add_single_prices("AB", prices))


if __name__ == "__main__":
    main()
