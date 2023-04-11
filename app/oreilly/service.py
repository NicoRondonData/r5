import requests

from app.base.settings import get_settings


async def get_books_oreilly(search_text):
    client = requests.Session()
    base_url = f"{get_settings().oreilly_api_url}search/?query={search_text}"
    response = client.get(base_url)
    return response.json().get("results", None)
