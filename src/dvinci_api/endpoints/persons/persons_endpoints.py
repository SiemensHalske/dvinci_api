"""
File: src/dvinci_api/endpoints/persons/persons_endpoints.py

Author: Hendrik Siemens
Date: 2024-07-30
Last modified: 2024-07-30
License: MIT

Description:
------------
Endpoints for the persons section of the d.vinci API.

Classes:
--------
- PersonsEndpoints: Class to encapsulate persons endpoints.

Methods:
--------
- get_persons: Get a list of permitted persons.
- post_person: Create a new person.
- get_person_by_external_id: Get a person with given externalId.
- get_person_by_id: Get a specific person.
- put_person: Update a person.
- delete_person: Delete a specific person.
- get_person_photo: Get photo for a specified person.
- post_person_photo: Add a photo for a specified person.
- delete_person_photo: Delete photo for a specified person.
"""

from ...client import DvinciClient


class PersonsEndpoints:
    """
    Class to encapsulate persons endpoints.

    Attributes:
    -----------
    client : DvinciClient
        An instance of the DvinciClient class to make requests to the API.
    """

    def __init__(self, client: DvinciClient):
        """
        Initialize the PersonsEndpoints with a DvinciClient instance.

        :param client: An instance of DvinciClient.
        """
        self.client = client

    def get_persons(self, **params):
        """
        Get a list of permitted persons.

        :param params: Query parameters for filtering persons.
        :return: List of persons.
        """
        return self.client.request("GET", "persons", params=params)

    def post_person(self, person_data: dict):
        """
        Create a new person.

        :param person_data: Dictionary containing person details.
        :return: Created person data.
        """
        return self.client.request("POST", "persons", json=person_data)

    def get_person_by_external_id(self, external_id: str):
        """
        Get a person with given externalId.

        :param external_id: External ID of the person.
        :return: Person data.
        """
        return self.client.request("GET", "persons", params={"externalId": external_id})

    def get_person_by_id(self, person_id: int):
        """
        Get a specific person.

        :param person_id: ID of the person.
        :return: Person data.
        """
        return self.client.request("GET", f"persons/{person_id}")

    def put_person(self, person_id: int, person_data: dict):
        """
        Update a person.

        :param person_id: ID of the person.
        :param person_data: Dictionary containing updated person details.
        :return: Updated person data.
        """
        return self.client.request("PUT", f"persons/{person_id}", json=person_data)

    def delete_person(self, person_id: int):
        """
        Delete a specific person.

        :param person_id: ID of the person.
        :return: Response data.
        """
        return self.client.request("POST", f"persons/{person_id}/delete")

    def get_person_photo(self, person_id: int):
        """
        Get photo for a specified person.

        :param person_id: ID of the person.
        :return: Photo data.
        """
        return self.client.request("GET", f"persons/{person_id}/photo")

    def post_person_photo(self, person_id: int, photo_data: dict):
        """
        Add a photo for a specified person.

        :param person_id: ID of the person.
        :param photo_data: Dictionary containing photo details.
        :return: Added photo data.
        """
        return self.client.request("POST", f"persons/{person_id}/photo", json=photo_data)

    def delete_person_photo(self, person_id: int):
        """
        Delete photo for a specified person.

        :param person_id: ID of the person.
        :return: Response data.
        """
        return self.client.request("POST", f"persons/{person_id}/photo/delete")
