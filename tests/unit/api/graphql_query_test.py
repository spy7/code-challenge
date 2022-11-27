from unittest import TestCase

from code_challenge.api.graphql_query import GraphQLQuery


class GraphQLQueryTestCase(TestCase):
    def test_treat_filter_value_text(self):
        self.assertEqual('"text"', GraphQLQuery.treat_filter_value("text"))

    def test_treat_filter_value_number(self):
        self.assertEqual('2', GraphQLQuery.treat_filter_value(2))

    def test_treat_filter_value_list(self):
        self.assertEqual(
            '[{x:1, y:"z"}]',
            GraphQLQuery.treat_filter_value([{"x": 1, "y": "z"}]),
        )

    def test_treat_filter(self):
        self.assertEqual(
            'x:1, y:"z"', GraphQLQuery.treat_filter({"x": 1, "y": "z"})
        )

    def test_treat_filter_with_list(self):
        self.assertEqual(
            'x:1, y:[{z:2}]',
            GraphQLQuery.treat_filter({"x": 1, "y": [{"z": 2}]}),
        )

    def test_create_command_no_filter_one_result(self):
        query = GraphQLQuery.create_command("run", {}, ["result"])
        self.assertEqual("{ run { result } }", query)

    def test_create_command_no_filter_two_results(self):
        query = GraphQLQuery.create_command("run", {}, ["result", "success"])
        self.assertEqual("{ run { result, success } }", query)

    def test_create_command_one_filter(self):
        query = GraphQLQuery.create_command("run", {"name": "x"}, ["result"])
        self.assertEqual('{ run(name:"x") { result } }', query)

    def test_create_command_two_filters(self):
        query = GraphQLQuery.create_command(
            "run", {"name": "x", "city": "y"}, ["result"]
        )
        self.assertEqual('{ run(name:"x", city:"y") { result } }', query)

    def test_create_query(self):
        query = GraphQLQuery.create_query("run", {}, ["result"])
        self.assertEqual("query { run { result } }", query)

    def test_create_mutation(self):
        query = GraphQLQuery.create_mutation("run", {}, ["result"])
        self.assertEqual("mutation { run { result } }", query)
