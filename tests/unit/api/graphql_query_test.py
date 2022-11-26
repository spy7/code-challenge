from unittest import TestCase

from code_challenge.api.graphql_query import GraphQLQuery


class GraphQLQueryTestCase(TestCase):
    def test_create_no_filter_one_result(self):
        query = GraphQLQuery.create("run", {}, ["result"])
        self.assertEqual("{ run { result } }", query)

    def test_create_no_filter_two_results(self):
        query = GraphQLQuery.create("run", {}, ["result", "success"])
        self.assertEqual("{ run { result, success } }", query)

    def test_create_one_filter(self):
        query = GraphQLQuery.create("run", {"name": "x"}, ["result"])
        self.assertEqual('{ run(name:"x") { result } }', query)

    def test_create_two_filters(self):
        query = GraphQLQuery.create("run", {"name": "x", "city": "y"}, ["result"])
        self.assertEqual('{ run(name:"x", city:"y") { result } }', query)
