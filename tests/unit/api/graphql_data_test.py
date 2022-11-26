from unittest import TestCase

from code_challenge.api.graphql_data import GraphQLData
from code_challenge.exceptions.code_challenge_exception import \
    CodeChallengeException


class GraphQLDataTestCase(TestCase):
    def test_treat(self):
        data = '{"data": {"run": {"x": 1, "y": 2} } }'
        df = GraphQLData.treat(data)
        self.assertEqual(1, df.shape[0])
        self.assertEqual(1, df["x"][0])
        self.assertEqual(2, df["y"][0])

    def test_treat_error(self):
        data = '{"data": {}, "errors": [{"message": "bad"}] }'
        with self.assertRaises(CodeChallengeException):
            GraphQLData.treat(data)
