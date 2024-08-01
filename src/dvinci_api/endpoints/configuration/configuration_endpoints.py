"""
File: src/dvinci_api/endpoints/configuration/configuration_endpoints.py

Author: Hendrik Siemens
Date: 2024-07-30
Last modified: 2024-07-30
License: MIT

Description:
------------
Endpoints for the configuration section of the d.vinci API.

Functions:
----------
- get_external_links(client: DvinciClient, config_type: str): Get a list of external links of
    the given type.
- put_external_links(client: DvinciClient, config_type: str, links_data: dict): Add or update
    a list of external links of the given type.
"""

from ...client import DvinciClient


def get_external_links(client: DvinciClient, config_type: str):
    """
    Get a list of external links of the given type.

    :param client: An instance of DvinciClient.
    :param config_type: Type of the configuration.
    :return: List of external links.
    """
    return client.request("GET", f"configuration/{config_type}/externalLinks")


def put_external_links(client: DvinciClient, config_type: str, links_data: dict):
    """
    Add or update a list of external links of the given type.

    :param client: An instance of DvinciClient.
    :param config_type: Type of the configuration.
    :param links_data: Dictionary containing links details.
    :return: Updated external links data.
    """
    return client.request("PUT", f"configuration/{config_type}/externalLinks", json=links_data)
