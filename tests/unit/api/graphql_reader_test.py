from unittest import TestCase
from unittest.mock import MagicMock, patch

from code_challenge.api.graphql_reader import GraphQLReader


@patch("code_challenge.api.graphql_reader.ConfigFile", MagicMock())
@patch("code_challenge.api.graphql_reader.requests.post")
class GraphQLReaderTestCase(TestCase):
    def test_query(self, post):
        post.return_value.text = "ok"
        result = GraphQLReader().query("{ run }")
        self.assertEqual("ok", result)
