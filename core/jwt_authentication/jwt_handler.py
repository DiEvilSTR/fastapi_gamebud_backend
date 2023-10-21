# This file is responsible for sighing, encoding, decoding and returning JWTs.
import time
import jwt

from core.config import settings


# Function used for signing the JWT string
def sign_jwt(uuid: str):
    payload = {
        "uuid": uuid,
        "expires": time.time() + settings.ACCESS_TOKEN_EXPIRE_MINUTES
    }
    token = jwt.encode(payload, settings.SECRET_KEY,
                       algorithm=settings.ALGORITHM)
    return {
        "access_token": token,
        "token_type": "bearer"
    }


# Function used for decoding token
def decode_jwt(token: str):
    try:
        decoded_token = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return None


# Function used for extracting uuid from token
def extract_username(token: str):
    try:
        return decode_jwt(token)["uuid"] if decode_jwt(token) else None
    except:
        return None
