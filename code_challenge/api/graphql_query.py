from typing import List, Dict, Optional


class GraphQLQuery:
    """Helper to create GraphQL query"""

    @classmethod
    def create(
        cls, command, filters: Dict[str, Optional[str]], responses: List[str]
    ) -> str:
        filter_str = ", ".join([f'{k}:"{v}"' for k, v in filters.items() if v])
        response_str = ", ".join(responses)
        if filter_str:
            filter_str = f"({filter_str})"
        return f"{{ {command}{filter_str} {{ {response_str} }} }}"
