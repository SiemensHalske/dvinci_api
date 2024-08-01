"""
File: src/dvinci_api/utils/verify_schemas.py

Author: Hendrik Siemens
Date: 2024-08-01
Last modified: 2024-08-01
License: MIT

Description:
------------
This module contains utility functions for verifying the schemas of the data
sent to different API endpoints. The schemas are defined in JSON files and
loaded dynamically based on the endpoint and method. The data is then validated
against the corresponding schema using the `jsonschema` library in Python to
ensure that it conforms to the expected structure.

Functions:
----------
verify_schema(schema_dir: str, endpoint: str, method: str, data: dict, response: bool = False):
    Verify the schema of the data for the given endpoint and method.

list_endpoints(schema_dir: str) -> list:
    List all available endpoints.

References:
-----------
"""
# flake8: noqa

import json
import os
import jsonschema
from jsonschema import validate


def _load_endpoint_schemas() -> dict:
    """
    Load the mapping of endpoints and methods to their respective schema
    files. This mapping is used to dynamically load the schema files when
    validating the data.

    :return: A dictionary mapping endpoints and methods to schema files.
    :rtype: dict
    """
    return {
        "GET /applications/": {
            "request": "applications/get_request",
            "response": "applications/get_response"
        },
        "POST /applications/": {
            "request": "applications/post_request",
            "response": "applications/post_response"
        },
        "PUT /applications/{id}": {
            "request": "applications/put_request",
            "response": "applications/put_response"
        },
        "POST /applications/{id}/delete": {
            "request": "applications/delete_request",
            "response": "applications/delete_response"
        },
        "POST /applications/{id}/statusChange/{statusId}": {
            "request": "applications/status_change_request",
            "response": "applications/status_change_response"
        },
        "POST /applications/{id}/jobOpeningMove/{jobOpeningId}": {
            "request": "applications/job_opening_move_request",
            "response": "applications/job_opening_move_response"
        },
        "GET /applications/{id}/attachments": {
            "request": "applications/attachments_get_request",
            "response": "applications/attachments_get_response"
        },
        "POST /applications/{id}/attachments": {
            "request": "applications/attachments_post_request",
            "response": "applications/attachments_post_response"
        },
        "GET /applications/{id}/attachments/{attachmentId}": {
            "request": "applications/attachment_id_get_request",
            "response": "applications/attachment_id_get_response"
        },
        "GET /applications/{id}/attachments/{attachmentId}/pdf": {
            "request": "applications/attachment_id_pdf_get_request",
            "response": "applications/attachment_id_pdf_get_response"
        },
        "GET /applications/{id}/history": {
            "request": "applications/history_get_request",
            "response": "applications/history_get_response"
        },
        "PUT /applications/{id}/history": {
            "request": "applications/history_put_request",
            "response": "applications/history_put_response"
        },
        "PUT /applications/{id}/history/{externalId}": {
            "request": "applications/history_external_id_put_request",
            "response": "applications/history_external_id_put_response"
        },
        # Add other endpoint and method mappings similarly if needed
    }


def _load_schema(schema_dir: str, schema_file: str) -> dict:
    """
    Load a schema from a file.

    :param schema_dir: The directory where the schema files are stored.
    :type schema_dir: str
    :param schema_file: The path to the schema file.
    :type schema_file: str
    :return: The loaded schema as a dictionary.
    :rtype: dict
    """
    schema_path = os.path.join(schema_dir, schema_file) + ".json"
    with open(schema_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def verify_schema(schema_dir: str, endpoint: str, method: str, data: dict, response: bool = False) -> bool:
    """
    Verify the schema of the data for the given endpoint and method.

    :param schema_dir: The directory where the schema files are stored.
    :type schema_dir: str
    :param endpoint: The endpoint for which the schema should be verified.
    :type endpoint: str
    :param method: The HTTP method (e.g., 'GET', 'POST', 'PUT', etc.).
    :type method: str
    :param data: The data that should be verified.
    :type data: dict
    :param response: Flag indicating whether to validate response data
        (default: False).
    :type response: bool
    :return: True if the data is valid, False otherwise.
    :rtype: bool
    """
    endpoint_schemas = _load_endpoint_schemas()
    endpoint_key = f"{method} {endpoint}"
    endpoint_schema = endpoint_schemas.get(endpoint_key)
    if endpoint_schema is None:
        print(f"Endpoint {endpoint_key} not found in schema mappings.")
        return False

    schema_file = endpoint_schema["response"] if response else endpoint_schema["request"]
    schema = _load_schema(schema_dir, schema_file)

    try:
        validate(instance=data, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        print(f"Schema validation error: {err}")
        return False

    return True


def list_endpoints() -> list:
    """
    List all available endpoints.

    :return: A list of available endpoints.
    :rtype: list
    """
    endpoint_schemas = _load_endpoint_schemas()
    return list(endpoint_schemas.keys())


# Example usage
if __name__ == "__main__":
    schema_dir = "../schemas"
    sample_data = {
        "externalId": "583988DC-1CD9-489B-A5D2-7D3E14712508",
        "languageId": "de",
        "version": 2,
        "comment": "This is a new comment!",
        "privacyPolicyAccepted": True,
        "extendedUseAccepted": True,
        "earliestStartingDate": "as soon as possible",
        "desiredSalary": "30.000$ per year",
        "hrServiceProviderEmail": "michael.mustermann@dvinci.de",
        "desiredLocations": ["HAMBURG"],
        "type": "ONLINE",
        "rating": "B",
        "sourceId": "MONSTER",
        "rejectionCodeId": None,
        "refJobPublication": {"id": 1},
        "refApplyDate": "2017-03-12",
        "screeningQuestions": [
            {
                "id": "MS_OFFICE_KNOWLEDGE",
                "answers": [{"id": "WORD"}, {"id": "EXCEL"}]
            },
            {
                "id": "MATH_MARK",
                "answers": [{"id": "MARK_4"}]
            },
            {
                "id": "JAVA_KNOWLEDGE",
                "answer": "3"
            }
        ]
    }
    is_valid = verify_schema(
        schema_dir, endpoint="/applications/{id}", method="PUT", data=sample_data, response=False)
    print(f"Data is valid: {is_va   lid}")

    # List all available endpoints
    endpoints = list_endpoints()
    print(f"Available endpoints: {endpoints}")
