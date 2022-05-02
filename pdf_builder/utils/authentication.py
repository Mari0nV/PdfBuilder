import os
from fastapi import Header

from pdf_builder.api.errors import InvalidToken


BUILDER_TOKEN = os.environ["BUILDER_TOKEN"]


async def verify_token(x_auth_token: str = Header(...)):
    if x_auth_token != BUILDER_TOKEN:
        raise InvalidToken()
