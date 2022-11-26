from code_challenge.api.graphql_reader import GraphQLReader
from code_challenge.services.company_service import CompanyService


def get_companies():
    reader = GraphQLReader()
    print(CompanyService(reader).get_companies())


if __name__ == "__main__":
    get_companies()
