from unittest import TestCase
from unittest.mock import MagicMock, patch
from code_challenge.models.company import Company

from code_challenge.services.company_service import CompanyService


@patch("code_challenge.services.company_service.GraphQLQuery", MagicMock())
class CompanyServiceTestCase(TestCase):
    def test_get_companies(self):
        reader = MagicMock()
        reader.query.return_value = {
            "data": {
                "companies": [
                    {
                        "name": "abc",
                        "ticker": "ABC",
                        "sector": "tech",
                        "country": "PT",
                    }
                ]
            }
        }
        response = CompanyService(reader).get_companies()
        self.assertEqual("abc", response[0].name)

    def test_get_ticker(self):
        company = Company(name="abc", ticker="ABC", sector="t", country="PT")
        self.assertEqual("ABC", CompanyService.get_ticker(company))
        self.assertEqual("xyz", CompanyService.get_ticker("xyz"))

    def test_get_prices(self):
        reader = MagicMock()
        reader.query.return_value = {"data": {"run": [{"x": 1, "y": 2}]}}
        response = CompanyService(reader).get_prices("ABC")
        self.assertEqual(1, response["x"][0])

    def test_get_recommendation(self):
        reader = MagicMock()
        reader.query.return_value = {"data": {"run": [{"toGrade": "Buy"}]}}
        response = CompanyService(reader).get_recommendation("ABC")
        self.assertEqual(1, response)

    def test_add_new_companies(self):
        reader = MagicMock()
        reader.mutation.return_value = {"data": {"run": [{"ok": "1"}]}}
        companies = [
            Company(name="abc", ticker="ABC", sector="tech", country="PT")
        ]
        response = CompanyService(reader).add_new_companies(companies)
        self.assertTrue(response)
