# This file is responsible for sighing, encoding, decoding and returning JWTs.
from fastapi import Response

import datetime
import jwt
import math
import time

from core.config import settings


def create_jwt_token(uuid: str):
    """
    Create JWT token

    Parameters:
    - **uuid**: User's uuid

    Returns:
    - **Token**: JWT token
    """
    payload = {
        "uuid": uuid,
        "expires": (time.time() + (settings.ACCESS_TOKEN_EXPIRE_SECONDS / 60))
    }
    token = jwt.encode(payload, settings.SECRET_KEY,
                       algorithm=settings.ALGORITHM)
    return token


# Not used in this project
def sign_jwt(uuid: str):
    """
    Sign JWT

    Parameters:
    - **uuid**: User's uuid

    Returns:
    - **Token**: JWT token
    """
    token = create_jwt_token(uuid)

    return {
        "access_token": token,
        "token_type": "bearer"
    }


def set_cookie_jwt(response: Response, uuid: str):
    """
    Set cookie JWT

    Parameters:
    - **response**: Response object
    - **uuid**: User's uuid
    """
    token = create_jwt_token(uuid)
    response.set_cookie(key=settings.AUTH_COOKIE_NAME, value=token, path="/",
                        httponly=True, samesite="lax", max_age=settings.ACCESS_TOKEN_EXPIRE_SECONDS)


def decode_jwt(token: str):
    """
    Decode JWT token

    Parameters:
    - **token**: JWT token

    Returns:
    - **Token**: Decoded JWT token or None
    """
    try:
        decoded_token = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return None
