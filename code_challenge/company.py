import requests


def get_companies():
    q = """{ companies {
        name
    } }"""

    headers = {"Authorization": "Bearer password"}
    resp = requests.post(
        "http://localhost:8000/graphql", json={"query": q}, headers=headers
    )
    print(resp.text)


if __name__ == "__main__":
    get_companies()
