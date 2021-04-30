import urllib.request
import json
from .models import Quote

# Getting the movie base url
base_url = None


def configure_request(app):
    global base_url
    base_url = app.config["QUOTE_API_BASE_URL"]


def get_quote():
    """
    Function that gets the json response to our url request
    """
    with urllib.request.urlopen(base_url) as url:
        quote_data = url.read()
        quote_response = json.loads(quote_data)
        quote_object = None
        if quote_response:
            id = quote_response.get("id")
            author = quote_response.get("author")
            quote = quote_response.get("quote")
            quote_object = Quote(id, author, quote)
    return quote_object
