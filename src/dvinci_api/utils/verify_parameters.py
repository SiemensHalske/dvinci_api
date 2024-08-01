"""
File: src/dvinci_api/utils/verify_parameters.py

Author: Hendrik Siemens
Date: 2024-08-01
Last modified: 2024-08-01
License: MIT

Description:
------------
This module contains utility functions for verifying parameters for different
API endpoints.

Classes:
--------

Methods:
--------

Functions:
----------
verify_applications_parameters(endpoint: str, **parameters: dict) -> bool:
    Verify the parameters for the given applications endpoint.

References:
-----------
"""
# flake8: noqa

# Dictionaries for the parameters of the different endpoints

APPLICATIONS_GET_PARAMETERS = {
    "query": {
        "byJobOpeningId": "number",
        "byJobOpeningExternalId": "string",
        "byApplicationStatusId": "string",
        "byOrgUnitId": "number",
        "byDateCreatedFrom": "date",
        "byDateCreatedTo": "date",
        "byLastStatusChangeDateFrom": "date",
        "byLastStatusChangeDateTo": "date",
    }
}

APPLICATIONS_EXTERNAL_ID_PARAMETERS = {
    "uri": {
        "externalId": "string",
    }
}

APPLICATIONS_ID_PARAMETERS = {
    "uri": {
        "id": "number",
    }
}

APPLICATIONS_ID_PUT_PARAMETERS = {
    "uri": {
        "id": "number",
    }
}

APPLICATIONS_ID_DELETE_PARAMETERS = {
    "uri": {
        "id": "number",
    }
}

APPLICATIONS_STATUS_CHANGE_PARAMETERS = {
    "uri": {
        "id": "number",
        "statusId": "number",
    }
}

APPLICATIONS_JOB_OPENING_MOVE_PARAMETERS = {
    "uri": {
        "id": "number",
        "jobOpeningId": "number",
    }
}

APPLICATIONS_ATTACHMENTS_PARAMETERS = {
    "uri": {
        "id": "number",
    }
}

APPLICATIONS_ATTACHMENT_ID_PARAMETERS = {
    "uri": {
        "id": "number",
        "attachmentId": "number",
    }
}

APPLICATIONS_ATTACHMENT_ID_PDF_PARAMETERS = {
    "uri": {
        "id": "number",
        "attachmentId": "number",
    }
}

APPLICATIONS_HISTORY_PARAMETERS = {
    "uri": {
        "id": "number",
    }
}

APPLICATIONS_HISTORY_EXTERNAL_ID_PARAMETERS = {
    "uri": {
        "id": "number",
        "externalId": "string",
    }
}

CONFIGURATION_EXTERNAL_LINKS_PARAMETERS = {
    "uri": {
        "type": "string",
    }
}

HIRING_REQUESTS_GET_PARAMETERS = {
    "query": {
        "byDateCreatedFrom": "date",
        "byDateCreatedTo": "date",
    }
}

HIRING_REQUESTS_EXTERNAL_ID_PARAMETERS = {
    "uri": {
        "externalId": "string",
    }
}

HIRING_REQUESTS_ID_PARAMETERS = {
    "uri": {
        "id": "number",
    }
}

HIRING_REQUESTS_HISTORY_PARAMETERS = {
    "uri": {
        "id": "number",
    }
}

HIRING_REQUESTS_APPROVERS_PARAMETERS = {
    "uri": {
        "id": "number",
    }
}

JOB_OPENINGS_GET_PARAMETERS = {
    "query": {
        "byDateCreatedFrom": "date",
        "byDateCreatedTo": "date",
    }
}

JOB_OPENINGS_EXTERNAL_ID_PARAMETERS = {
    "uri": {
        "externalId": "string",
    }
}

JOB_OPENINGS_ID_PARAMETERS = {
    "uri": {
        "id": "number",
    }
}

JOB_OPENINGS_HISTORY_PARAMETERS = {
    "uri": {
        "id": "number",
    }
}

JOB_OPENINGS_HISTORY_EXTERNAL_ID_PARAMETERS = {
    "uri": {
        "id": "number",
        "externalId": "string",
    }
}

JOB_PUBLICATIONS_EXTERNAL_ID_PARAMETERS = {
    "uri": {
        "externalId": "string",
    }
}

JOB_PUBLICATIONS_ID_PARAMETERS = {
    "uri": {
        "id": "number",
    }
}

JOB_PUBLICATIONS_DELETE_PARAMETERS = {
    "uri": {
        "id": "number",
    }
}

JOB_PUBLICATION_CHANNELS_ID_PARAMETERS = {
    "uri": {
        "id": "string",
    }
}

JOB_PUBLICATION_PLACEMENTS_PARAMETERS = {
    "uri": {
        "partner_id": "string",
    }
}

JOB_PUBLICATION_PLACEMENTS_EXTERNAL_ID_PARAMETERS = {
    "uri": {
        "partner_id": "string",
        "externalId": "string",
    }
}

JOB_PUBLICATION_PLACEMENTS_JOB_PUBLICATION_ID_PARAMETERS = {
    "uri": {
        "partner_id": "string",
        "jobPublicationId": "number",
    }
}

JOB_PUBLICATION_PLACEMENTS_ID_PARAMETERS = {
    "uri": {
        "partner_id": "string",
        "id": "number",
    }
}

LOCATIONS_GET_PARAMETERS = {
    "query": {
        "forJobOpeningByOrgUnitId": "number",
    }
}

LOCATIONS_ID_PARAMETERS = {
    "uri": {
        "id": "string",
    }
}

ONBOARDINGS_GET_PARAMETERS = {
    "query": {
        "status": "string",
        "orgUnitId": "integer",
        "applicationId": "integer",
        "fromDateOfStart": "string",
        "fromDateOfContract": "string",
        "fromDateOfEmployment": "string",
        "fromDateOfEnd": "string",
        "fromDateCreated": "string",
    }
}

ONBOARDINGS_ID_PARAMETERS = {
    "uri": {
        "id": "number",
    }
}

ONBOARDINGS_ATTACHMENT_ID_PARAMETERS = {
    "uri": {
        "id": "number",
        "attachmentId": "string",
    }
}

ORG_UNITS_ID_PARAMETERS = {
    "uri": {
        "id": "number",
    }
}

PERSONS_EXTERNAL_ID_PARAMETERS = {
    "uri": {
        "externalId": "string",
    }
}

PERSONS_ID_PARAMETERS = {
    "uri": {
        "id": "number",
    }
}

USERS_GET_PARAMETERS = {
    "query": {
        "lang": "string",
        "externalId": "string",
        "forJobOpeningByOrgUnitId": "number",
    }
}

USERS_ID_PARAMETERS = {
    "uri": {
        "id": "number",
    }
}

USER_GROUPS_GET_PARAMETERS = {
    "query": {
        "forJobOpeningByOrgUnitId": "number",
        "externalId": "string",
    }
}

USER_GROUPS_ID_PARAMETERS = {
    "uri": {
        "id": "number",
    }
}

# Mapping of endpoints to their respective parameter dictionaries
ENDPOINT_PARAMETERS = {
    "/applications/": APPLICATIONS_GET_PARAMETERS,
    "/applications/?externalId={externalId}": APPLICATIONS_EXTERNAL_ID_PARAMETERS,
    "/applications/{id}": APPLICATIONS_ID_PARAMETERS,
    "/applications/{id} (PUT)": APPLICATIONS_ID_PUT_PARAMETERS,
    "/applications/{id}/delete": APPLICATIONS_ID_DELETE_PARAMETERS,
    "/applications/{id}/statusChange/{statusId}": APPLICATIONS_STATUS_CHANGE_PARAMETERS,
    "/applications/{id}/jobOpeningMove/{jobOpeningId}": APPLICATIONS_JOB_OPENING_MOVE_PARAMETERS,
    "/applications/{id}/attachments": APPLICATIONS_ATTACHMENTS_PARAMETERS,
    "/applications/{id}/attachments/{attachmentId}": APPLICATIONS_ATTACHMENT_ID_PARAMETERS,
    "/applications/{id}/attachments/{attachmentId}/pdf": APPLICATIONS_ATTACHMENT_ID_PDF_PARAMETERS,
    "/applications/{id}/history": APPLICATIONS_HISTORY_PARAMETERS,
    "/applications/{id}/history/{externalId}": APPLICATIONS_HISTORY_EXTERNAL_ID_PARAMETERS,
    "/configuration/{type}/externalLinks (GET)": CONFIGURATION_EXTERNAL_LINKS_PARAMETERS,
    "/configuration/{type}/externalLinks (PUT)": CONFIGURATION_EXTERNAL_LINKS_PARAMETERS,
    "/hiringRequests/": HIRING_REQUESTS_GET_PARAMETERS,
    "/hiringRequests/?externalId={externalId}": HIRING_REQUESTS_EXTERNAL_ID_PARAMETERS,
    "/hiringRequests/{id}": HIRING_REQUESTS_ID_PARAMETERS,
    "/hiringRequests/{id}/history": HIRING_REQUESTS_HISTORY_PARAMETERS,
    "/hiringRequests/{id}/approvers": HIRING_REQUESTS_APPROVERS_PARAMETERS,
    "/jobOpenings/": JOB_OPENINGS_GET_PARAMETERS,
    "/jobOpenings/?externalId={externalId}": JOB_OPENINGS_EXTERNAL_ID_PARAMETERS,
    "/jobOpenings/{id}": JOB_OPENINGS_ID_PARAMETERS,
    "/jobOpenings/{id}/history": JOB_OPENINGS_HISTORY_PARAMETERS,
    "/jobOpenings/{id}/history/{externalId}": JOB_OPENINGS_HISTORY_EXTERNAL_ID_PARAMETERS,
    "/jobPublications/?externalId={externalId}": JOB_PUBLICATIONS_EXTERNAL_ID_PARAMETERS,
    "/jobPublications/{id}": JOB_PUBLICATIONS_ID_PARAMETERS,
    "/jobPublications/{id}/delete": JOB_PUBLICATIONS_DELETE_PARAMETERS,
    "/jobPublicationChannels/{id}": JOB_PUBLICATION_CHANNELS_ID_PARAMETERS,
    "/jobPublicationPlacements/{partner_id}/placements": JOB_PUBLICATION_PLACEMENTS_PARAMETERS,
    "/jobPublicationPlacements/{partner_id}/placements/?externalId={externalId}": JOB_PUBLICATION_PLACEMENTS_EXTERNAL_ID_PARAMETERS,
    "/jobPublicationPlacements/{partner_id}/placements/?jobPublicationId={jobPublicationId}": JOB_PUBLICATION_PLACEMENTS_JOB_PUBLICATION_ID_PARAMETERS,
    "/jobPublicationPlacements/{partner_id}/placements/{id}": JOB_PUBLICATION_PLACEMENTS_ID_PARAMETERS,
    "/jobPublicationPlacements/{partner_id}/placements/{id} (PUT)": JOB_PUBLICATION_PLACEMENTS_ID_PARAMETERS,
    "/jobPublicationPlacements/{partner_id}/placements/{id}/delete": JOB_PUBLICATION_PLACEMENTS_ID_PARAMETERS,
    "/locations/": LOCATIONS_GET_PARAMETERS,
    "/locations/{id}": LOCATIONS_ID_PARAMETERS,
    "/onboardings/": ONBOARDINGS_GET_PARAMETERS,
    "/onboardings/{id}": ONBOARDINGS_ID_PARAMETERS,
    "/onboardings/{id}/attachments": ONBOARDINGS_ID_PARAMETERS,
    "/onboardings/{id}/attachments/{attachmentId}": ONBOARDINGS_ATTACHMENT_ID_PARAMETERS,
    "/onboardings/{id}/attachments/{attachmentId}/pdf": ONBOARDINGS_ATTACHMENT_ID_PARAMETERS,
    "/onboardings/{id}/delete": ONBOARDINGS_ID_PARAMETERS,
    "/orgUnits/{id}": ORG_UNITS_ID_PARAMETERS,
    "/persons/?externalId={externalId}": PERSONS_EXTERNAL_ID_PARAMETERS,
    "/persons/{id}": PERSONS_ID_PARAMETERS,
    "/persons/{id} (PUT)": PERSONS_ID_PARAMETERS,
    "/persons/{id}/delete": PERSONS_ID_PARAMETERS,
    "/persons/{id}/photo": PERSONS_ID_PARAMETERS,
    "/persons/{id}/photo/delete": PERSONS_ID_PARAMETERS,
    "/users/": USERS_GET_PARAMETERS,
    "/users/{id}": USERS_ID_PARAMETERS,
    "/users/{id} (PUT)": USERS_ID_PARAMETERS,
    "/users/{id}/delete": USERS_ID_PARAMETERS,
    "/userGroups/": USER_GROUPS_GET_PARAMETERS,
    "/userGroups/{id}": USER_GROUPS_ID_PARAMETERS,
    "/userGroups/{id} (PUT)": USER_GROUPS_ID_PARAMETERS,
    "/userGroups/{id}/delete": USER_GROUPS_ID_PARAMETERS,
}


def verify_applications_parameters(endpoint: str, **parameters: dict) -> bool:
    """
    Verify the parameters for the given applications endpoint.

    :param endpoint: The endpoint for which the parameters should be verified.
    :type endpoint: str
    :param parameters: The parameters that should be verified.
    :type parameters: dict
    :return: True if the parameters are valid, False otherwise.
    :rtype: bool
    """

    endpoint_parameters = ENDPOINT_PARAMETERS.get(endpoint)

    if endpoint_parameters is None:
        return False

    for parameter_type, parameter_value in parameters.items():
        if parameter_type not in endpoint_parameters:
            return False

        parameter_type_value = endpoint_parameters[parameter_type]

        if parameter_type_value != parameter_value:
            return False

    # Additional check if all required parameters are present
    for required_parameter in endpoint_parameters:
        if required_parameter not in parameters:
            return False

    return True
