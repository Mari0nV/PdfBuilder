from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder


class ApiException(HTTPException):
    def __init__(self, status_code: int, error: dict):
        super().__init__(
            status_code, jsonable_encoder({"error": type(self).__name__, **error})
        )


class InvalidToken(ApiException):
    def __init__(self):
        super().__init__(
            401,
            {
                "message": ("Provided X-Auth-Token is invalid"),
            },
        )


class ContentTypeNotSupported(ApiException):
    def __init__(self, content_type: str):
        super().__init__(
            415,
            {
                "message": (f"Content type {content_type} is not supported."),
            },
        )