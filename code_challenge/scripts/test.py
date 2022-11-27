from code_challenge.api.config_file import ConfigFile
from code_challenge.api.graphql_reader import GraphQLReader
from code_challenge.services.company_service import CompanyService


def main():
    settings = ConfigFile().read()
    reader = GraphQLReader(settings)
    service = CompanyService(reader)
    df = service.get_recommendation("AAPL", "2022-11-01")
    print(df)


if __name__ == "__main__":
    main()
