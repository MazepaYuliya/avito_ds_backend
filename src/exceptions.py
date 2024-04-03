from requests import HTTPError


class RequestsNotFoundException(HTTPError):
    def __init__(self, *args, **kwargs):
        super().__init__()


class RequestsUnavailableException(HTTPError):
    def __init__(self, *args, **kwargs):
        super().__init__()
