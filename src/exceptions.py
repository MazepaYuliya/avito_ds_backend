"""Module with custom exceptions"""
from requests import HTTPError


class RequestsNotFoundException(HTTPError):
    """Exception for error 404"""
    def __init__(self, *args, **kwargs):
        super().__init__()


class RequestsUnavailableException(HTTPError):
    """Exception for error 504"""
    def __init__(self, *args, **kwargs):
        super().__init__()
