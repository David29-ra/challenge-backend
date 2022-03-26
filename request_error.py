class RequestError(Exception):
    """
    Raise this error when the request fails.

    Attributes:
        status_code -- input salary which caused the error
        message -- explanation of the error
    """
    def __init__(self, status_code, url, message = "Error in the request for url"):
        self.status_code = status_code
        self.message = message + ": {}".format(url)
        super().__init__(self.message)