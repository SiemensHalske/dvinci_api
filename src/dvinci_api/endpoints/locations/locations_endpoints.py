"""
File: src/dvinci_api/endpoints/locations/locations_endpoints.py

Author: Hendrik Siemens
Date: 2024-07-30
Last modified: 2024-07-30
License: MIT

Description:
------------
Endpoints for the locations section of the d.vinci API.

Classes:
--------
- LocationsEndpoints: Class to encapsulate locations endpoints.

Methods:
--------
- get_locations: Get a list of locations.
- post_location: Create a new location.
- get_location_by_id: Get a specific location.
- put_location: Update a location.
- delete_location: Delete a specific location.
"""

from ...client import DvinciClient


class LocationsEndpoints:
    """
    Class to encapsulate locations endpoints.

    Attributes:
    -----------
    client : DvinciClient
        An instance of the DvinciClient class to make requests to the API.
    """

    def __init__(self, client: DvinciClient):
        """
        Initialize the LocationsEndpoints with a DvinciClient instance.

        :param client: An instance of DvinciClient.
        """
        self.client = client

    def get_locations(self, **params):
        """
        Get a list of locations.

        :param params: Query parameters for filtering locations.
        :return: List of locations.
        """
        return self.client.request("GET", "locations", params=params)

    def post_location(self, location_data: dict):
        """
        Create a new location.

        :param location_data: Dictionary containing location details.
        :return: Created location data.
        """
        return self.client.request("POST", "locations", json=location_data)

    def get_location_by_id(self, location_id: int):
        """
        Get a specific location.

        :param location_id: ID of the location.
        :return: Location data.
        """
        return self.client.request("GET", f"locations/{location_id}")

    def put_location(self, location_id: int, location_data: dict):
        """
        Update a location.

        :param location_id: ID of the location.
        :param location_data: Dictionary containing updated location details.
        :return: Updated location data.
        """
        return self.client.request("PUT", f"locations/{location_id}", json=location_data)

    def delete_location(self, location_id: int):
        """
        Delete a specific location.

        :param location_id: ID of the location.
        :return: Response data.
        """
        return self.client.request("POST", f"locations/{location_id}/delete")
