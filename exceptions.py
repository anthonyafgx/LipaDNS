class APIRequestError(Exception):
    def __init__(self, message:str="API request failed", errors: (dict[str,str] | None) = None):
        super().__init__(message)
        self.errors = errors