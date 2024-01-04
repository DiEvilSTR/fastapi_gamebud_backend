# The function of this file is to check whether the request is authorized or not [Verification of the protected route]
from fastapi import Request, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .jwt_handler import decode_jwt
from core.config import settings


class JWTBearer(HTTPBearer):
    """
    JWTBearer class

    This class is used to verify the JWT token sent in cookies.
    """

    def __init__(self, auto_error: bool = True, cookie_name: str = settings.AUTH_COOKIE_NAME):
        """
        Constructor method

        Parameters:
        - **auto_error**: If True, will raise HTTPException if the token is invalid or expired.
        - **cookie_name**: The name of the cookie containing the JWT token.
        """
        super(JWTBearer, self).__init__(auto_error=auto_error)
        self.cookie_name = cookie_name

    async def __call__(self, request: Request):
        """
        Call method

        Parameters:
        - **request**: Request object with the cookie containing the token.
        """
        token = request.cookies.get(self.cookie_name)
        
        if token:
            if not self.verify_jwt(token):
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token or expired token."
                )
            return self.get_user_uuid(token)
        else:
            if self.auto_error:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED, detail="Token not found in cookies."
                )
            return None


    def verify_jwt(self, jwtoken: str):
        is_token_valid: bool = False  # A false flag

        try:
            payload = decode_jwt(jwtoken)
        except:
            payload = None

        if payload:
            is_token_valid = True
        return is_token_valid

    @staticmethod
    def get_user_uuid(jwtoken: str) -> str:
        try:
            uuid = decode_jwt(jwtoken)["uuid"]
        except:
            uuid = None
        return uuid


jwt_scheme = JWTBearer()