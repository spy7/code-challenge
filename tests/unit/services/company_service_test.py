from unittest import TestCase
from unittest.mock import MagicMock, patch
from code_challenge.models.company import Company
from code_challenge.models.price import Price
from code_challenge.models.recommendation import Recommendation

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
        reader.query.return_value = {
            "data": {"run": [{"date": "2022-11-15", "toGrade": "Buy"}]}
        }
        response = CompanyService(reader).get_recommendation("ABC")
        self.assertEqual(1.0, response["average"][0])

    def test_add_new_companies(self):
        reader = MagicMock()
        reader.query.return_value = {"data": {"run": [{"ok": "1"}]}}
        companies = [
            Company(name="abc", ticker="ABC", sector="tech", country="PT")
        ]
        response = CompanyService(reader).add_new_companies(companies)
        self.assertTrue(response)

    def test_add_prices(self):
        reader = MagicMock()
        reader.query.return_value = {"data": {"run": {"status": "OK"}}}
        prices = [Price("2022-11-15", 2, 3, 2, 2.5, 10)]
        response = CompanyService(reader).add_prices("ABC", prices)
        self.assertTrue(response)

    def test_add_single_price(self):
        reader = MagicMock()
        reader.query.return_value = {"data": {"run": {"status": "OK"}}}
        response = CompanyService(reader).add_single_price(
            "ABC", "2022-11-15", 2, 3, 2, 2.5, 10
        )
        self.assertTrue(response)

    def test_add_recommendations(self):
        reader = MagicMock()
        reader.query.return_value = {"data": {"run": {"status": "OK"}}}
        recommendations = [
            Recommendation("2022-11-15", "fgh", "Negative", "Buy")
        ]
        response = CompanyService(reader).add_recommendations(
            "ABC", recommendations
        )
        self.assertTrue(response)

    def test_add_single_recommendation(self):
        reader = MagicMock()
        reader.query.return_value = {"data": {"run": {"status": "OK"}}}
        response = CompanyService(reader).add_single_recommendation(
            "ABC", "2022-11-15", "fgh", "Negative", "Buy"
        )
        self.assertTrue(response)
