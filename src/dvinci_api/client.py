"""
File: src/dvinci_api/client.py

Author: Hendrik Siemens
Date: 2024-07-30
Last modified: 2024-07-30
License: MIT

Description:
------------
Python client for the d.vinci API.

Classes:
--------
- DvinciClient: Client for the d.vinci API.

Methods:
--------
- _request(method: str, endpoint: str, **kwargs): Internal method to make a request to
    the d.vinci API.
- request(method: str, endpoint: str, **kwargs): Public method to make a request to the
    d.vinci API.
- get_status(): Public method to check the status of the API.

Functions:
----------

References:
-----------
"""
import requests
from .exceptions import DvinciAPIAuthError, DvinciAPIRequestError


class DvinciClient:
    """
    Client for the d.vinci API.

    Attributes:
    -----------
    - api_user (str): API user name.
    - api_token (str): API token.
    - base_url (str): Base URL for the d.vinci API.
    - headers (dict): HTTP headers for the API requests.

    Methods:
    --------
    - _request(method: str, endpoint: str, **kwargs): Internal method to make a request to
        the d.vinci API.
    - request(method: str, endpoint: str, **kwargs): Public method to make a request to the
        d.vinci API.
    - get_status(): Public method to check the status of the API.

    """

    def __init__(self, api_user: str, api_token: str, customer: str):
        """
        Initialize the DvinciClient with the necessary authentication details.

        :param api_user: API user name.
        :param api_token: API token.
        :param customer: Customer identifier for the d.vinci API.
        """
        self.api_user = api_user
        self.api_token = api_token
        self.base_url = f"https://{customer}.dvinci.de/restApi"
        self.headers = {
            "Accept": "application/json",
            "Dvinci-API-User": self.api_user,
            "Dvinci-API-Token": self.api_token
        }

    def _request(self, method: str, endpoint: str, **kwargs):
        """
        Internal method to make a request to the d.vinci API.

        :param method: HTTP method (e.g., 'GET', 'POST').
        :param endpoint: API endpoint to call.
        :param kwargs: Additional arguments for the requests method.
        :return: Response from the API in JSON format.
        """
        url = f"{self.base_url}/{endpoint}"
        response = requests.request(
            method, url, headers=self.headers, **kwargs, timeout=10)

        if response.status_code == 401:
            raise DvinciAPIAuthError(response.status_code, response.text)
        elif not response.ok:
            raise DvinciAPIRequestError(response.status_code, response.text)

        return response.json()

    def request(self, method: str, endpoint: str, **kwargs):
        """
        Public method to make a request to the d.vinci API.

        :param method: HTTP method (e.g., 'GET', 'POST').
        :param endpoint: API endpoint to call.
        :param kwargs: Additional arguments for the requests method.
        :return: Response from the API in JSON format.
        """
        return self._request(method, endpoint, **kwargs)

    def get_status(self):
        """
        Public method to check the status of the API.

        :return: API status in JSON format.
        """
        return self._request("GET", "status")

    def __str__(self):
        return f"DvinciClient({self.api_user}, {self.base_url})"
