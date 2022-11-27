from unittest import TestCase
from unittest.mock import MagicMock, patch

from code_challenge.api.graphql_reader import GraphQLReader


@patch("code_challenge.api.graphql_reader.requests.post")
class GraphQLReaderTestCase(TestCase):
    def test_query(self, post):
        post.return_value.json.return_value = {"ok": 1}
        settings = MagicMock()
        result = GraphQLReader(settings).query("{ run }")
        self.assertEqual(1, result["ok"])
