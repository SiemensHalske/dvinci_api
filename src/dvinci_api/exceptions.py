"""
File: src/dvinci_api/exceptions.py

Author: Hendrik Siemens
Date: 2024-07-30
Last modified: 2024-07-30
License: MIT

Description:
------------
Custom exceptions for the d.vinci API client.

Classes:
--------
- DvinciAPIError: Base class for all d.vinci API errors.
- DvinciAPIAuthError: Exception for authentication errors.
- DvinciAPIRequestError: Exception for request errors.
"""


class DvinciAPIError(Exception):
    """
    Base class for all d.vinci API errors.

    Attributes:
    -----------
    - status_code (int): HTTP status code of the error.
    - message (str): Error message.

    Methods:
    --------
    - __str__(): Returns the string representation of the error.
    """

    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message
        super().__init__(f"Error {status_code}: {message}")

    def __str__(self):
        return f"DvinciAPIError(status_code={self.status_code}, message={self.message})"


class DvinciAPIAuthError(DvinciAPIError):
    """
    Exception for authentication errors.
    """

    def __init__(self, status_code, message="Authentication failed"):
        super().__init__(status_code, message)


class DvinciAPIRequestError(DvinciAPIError):
    """
    Exception for request errors.
    """

    def __init__(self, status_code, message="Request failed"):
        super().__init__(status_code, message)
