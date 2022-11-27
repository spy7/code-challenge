from typing import List, Dict


class GraphQLQuery:
    """Helper to create GraphQL query"""

    @classmethod
    def treat_filter_value(cls, filter_value) -> str:
        if isinstance(filter_value, list):
            filter_list = ", ".join(
                cls.treat_filter_value(item) for item in filter_value
            )
            return f"[{filter_list}]"
        if isinstance(filter_value, Dict):
            return f"{{{cls.treat_filter(filter_value)}}}"
        if isinstance(filter_value, str):
            return f'"{filter_value}"'
        return f"{filter_value}"

    @classmethod
    def treat_filter(cls, filters: Dict) -> str:
        return ", ".join(
            [
                f"{k}:{cls.treat_filter_value(v)}"
                for k, v in filters.items()
                if v is not None
            ]
        )

    @classmethod
    def create_command(
        cls, command, filters: Dict, responses: List[str]
    ) -> str:
        filter_str = cls.treat_filter(filters)
        response_str = ", ".join(responses)
        if filter_str:
            filter_str = f"({filter_str})"
        return f"{{ {command}{filter_str} {{ {response_str} }} }}"

    @classmethod
    def create_query(cls, command, filters: Dict, responses: List[str]) -> str:
        return f"query {cls.create_command(command, filters, responses)}"

    @classmethod
    def create_mutation(
        cls, command, filters: Dict, responses: List[str]
    ) -> str:
        return f"mutation {cls.create_command(command, filters, responses)}"
