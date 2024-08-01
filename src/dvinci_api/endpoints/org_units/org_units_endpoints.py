"""
File: src/dvinci_api/endpoints/org_units/org_units_endpoints.py

Author: Hendrik Siemens
Date: 2024-07-30
Last modified: 2024-07-30
License: MIT

Description:
------------
Endpoints for the organisation units section of the d.vinci API.

Classes:
--------
- OrgUnitsEndpoints: Class to encapsulate organisation units endpoints.

Methods:
--------
- get_org_units: Get a list of all configured organisation units your API user is permitted to.
- get_org_unit_by_id: Get a specific organisation unit.
"""

from ...client import DvinciClient


class OrgUnitsEndpoints:
    """
    Class to encapsulate organisation units endpoints.

    Attributes:
    -----------
    client : DvinciClient
        An instance of the DvinciClient class to make requests to the API.
    """

    def __init__(self, client: DvinciClient):
        """
        Initialize the OrgUnitsEndpoints with a DvinciClient instance.

        :param client: An instance of DvinciClient.
        """
        self.client = client

    def get_org_units(self):
        """
        Get a list of all configured organisation units your API user is permitted to.

        :return: List of organisation units.
        """
        return self.client.request("GET", "orgUnits")

    def get_org_unit_by_id(self, unit_id: int):
        """
        Get a specific organisation unit.

        :param unit_id: ID of the organisation unit.
        :return: Organisation unit data.
        """
        return self.client.request("GET", f"orgUnits/{unit_id}")
