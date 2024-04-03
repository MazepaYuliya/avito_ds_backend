"""Module with custom exceptions"""
from requests import HTTPError
from requests.exceptions import RequestException


class RequestsNotFoundException(HTTPError):
    """Exception for error 404"""
    def __init__(self, *args, **kwargs):
        super().__init__()


class RequestsUnavailableException(HTTPError, RequestException):
    """Exception for error 504"""
    def __init__(self, *args, **kwargs):
        super().__init__()
