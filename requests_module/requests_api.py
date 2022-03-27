import requests

from requests_module.request_error import RequestError

def api_response(url) -> dict or str:
    """
    Return the response of the api in json format.
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise RequestError(response.status_code, url)
