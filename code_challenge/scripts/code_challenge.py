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
    # prices = [
    #     Price(date="2022-11-11", open=2, high=3, low=2, close=2.5, volume=10)
    # ]
    # print(service.add_prices("AB", prices))
    # print(service.add_single_price("AB", "2022-11-12", 2, 3, 2, 2, 5))
    print(service.update_price("AB", "2022-11-13", 2, 4))


if __name__ == "__main__":
    main()
