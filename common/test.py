import logging
import random
import requests
import string

# Constants
BASE_URL = "https://rest-api-store-item.herokuapp.com"

METHOD_GET = "GET"
METHOD_POST = "POST"
METHOD_PUT = "PUT"
METHOD_DELETE = "DELETE"

REQ_URLS = {
    "store": "/store/",
    "stores": "/stores",
    "item": "/item/",
    "items": "/items",
    "register": "/register",
}

# Logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler("log.log")
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


def make_url(req_url: str, value: str = None) -> str:
    result = f"{BASE_URL}{req_url}"
    if value:
        result += value
    return result


def generate_random_str(length: int = 5, chars=string.ascii_letters) -> str:
    return "".join(random.choice(chars) for _ in range(length))


def make_request(method: str, url: str) -> requests.Response:
    logger.debug(f"Sending {str.upper(method)} request: {url}")
    response = requests.request(method=method, url=url)
    logger.debug(f"Got response: {response.json()}")
    return response


def add_store() -> None:
    make_request(METHOD_POST, make_url(REQ_URLS["store"], generate_random_str()))


def get_all_stores() -> dict:
    return make_request(METHOD_GET, make_url(REQ_URLS["stores"])).json()


def delete_store(store_name) -> None:
    make_request(METHOD_DELETE, make_url(REQ_URLS["store"], store_name))


def log_separator() -> None:
    logger.debug("-" * 72)
