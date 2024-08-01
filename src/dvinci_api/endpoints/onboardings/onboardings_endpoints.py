"""
File: src/dvinci_api/endpoints/onboardings/onboardings_endpoints.py

Author: Hendrik Siemens
Date: 2024-07-30
Last modified: 2024-07-30
License: MIT

Description:
------------
Endpoints for the onboardings section of the d.vinci API.

Classes:
--------
- OnboardingsEndpoints: Class to encapsulate onboardings endpoints.

Methods:
--------
- get_onboardings: Get a list of all onboardings your API user is permitted to.
- get_onboarding_by_id: Get a specific onboarding.
- get_onboarding_attachments: Get all attachments for the given onboarding id.
- get_onboarding_attachment_by_id: Get attachment for the given onboarding id and attachment id.
- get_onboarding_attachment_pdf: Get converted version (always a pdf) of the attachment for the
    given onboarding id and attachment id.
- delete_onboarding: Delete a specific onboarding.
"""

from ...client import DvinciClient


class OnboardingsEndpoints:
    """
    Class to encapsulate onboardings endpoints.

    Attributes:
    -----------
    client : DvinciClient
        An instance of the DvinciClient class to make requests to the API.
    """

    def __init__(self, client: DvinciClient):
        """
        Initialize the OnboardingsEndpoints with a DvinciClient instance.

        :param client: An instance of DvinciClient.
        """
        self.client = client

    def get_onboardings(self):
        """
        Get a list of all onboardings your API user is permitted to.

        :return: List of onboardings.
        """
        return self.client.request("GET", "onboardings")

    def get_onboarding_by_id(self, onboarding_id: int):
        """
        Get a specific onboarding.

        :param onboarding_id: ID of the onboarding.
        :return: Onboarding data.
        """
        return self.client.request("GET", f"onboardings/{onboarding_id}")

    def get_onboarding_attachments(self, onboarding_id: int):
        """
        Get all attachments for the given onboarding id.

        :param onboarding_id: ID of the onboarding.
        :return: List of attachments.
        """
        return self.client.request("GET", f"onboardings/{onboarding_id}/attachments")

    def get_onboarding_attachment_by_id(self, onboarding_id: int, attachment_id: int):
        """
        Get attachment for the given onboarding id and attachment id.

        :param onboarding_id: ID of the onboarding.
        :param attachment_id: ID of the attachment.
        :return: Attachment data.
        """
        return self.client.request("GET", f"onboardings/{onboarding_id}/attachments/{attachment_id}")

    def get_onboarding_attachment_pdf(self, onboarding_id: int, attachment_id: int):
        """
        Get converted version (always a pdf) of the attachment for the given onboarding id and attachment id.

        :param onboarding_id: ID of the onboarding.
        :param attachment_id: ID of the attachment.
        :return: PDF version of the attachment.
        """
        return self.client.request("GET", f"onboardings/{onboarding_id}/attachments/{attachment_id}/pdf")

    def delete_onboarding(self, onboarding_id: int):
        """
        Delete a specific onboarding.

        :param onboarding_id: ID of the onboarding.
        :return: Response data.
        """
        return self.client.request("POST", f"onboardings/{onboarding_id}/delete")
