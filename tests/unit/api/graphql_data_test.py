from unittest import TestCase

from code_challenge.api.graphql_data import GraphQLData
from code_challenge.exceptions.code_challenge_exception import (
    CodeChallengeException,
)


class GraphQLDataTestCase(TestCase):
    sample_data = {"data": {"run": [{"x": 1, "y": 2}]}}
    error_data = {"data": {}, "errors": [{"message": "bad"}]}

    def test_validate_response(self):
        self.assertIsNone(GraphQLData.validate_response(self.sample_data))

    def test_validate_response_error(self):
        with self.assertRaises(CodeChallengeException):
            GraphQLData.validate_response(self.error_data)

    def test_verify_status_ok(self):
        data = {"data": {"addPrices": {"status": "OK"}}}
        self.assertTrue(GraphQLData.verify_status(data))

    def test_verify_status_false(self):
        data = {"data": {"addPrices": {"status": "ERROR"}}}
        self.assertFalse(GraphQLData.verify_status(data))

    def test_extract_data(self):
        data = GraphQLData.extract_data(self.sample_data)
        self.assertEqual(1, len(data))
        self.assertEqual(1, data[0]["x"])
        self.assertEqual(2, data[0]["y"])

    def test_convert_to_data_frame(self):
        df = GraphQLData.convert_to_data_frame(self.sample_data)
        self.assertEqual(1, df.shape[0])
        self.assertEqual(1, df["x"][0])
        self.assertEqual(2, df["y"][0])

    def test_convert_to_companies(self):
        company_data = {
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
        companies = GraphQLData.convert_to_companies(company_data)
        self.assertEqual(1, len(companies))
        self.assertEqual("abc", companies[0].name)
        self.assertEqual("ABC", companies[0].ticker)
        self.assertEqual("tech", companies[0].sector)
        self.assertEqual("PT", companies[0].country)
