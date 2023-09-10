from pydantic import BaseModel, EmailStr


class Token(BaseModel):
    """
    Token class

    Fields:
    - **access_token**: Access token
    - **token_type**: Token type
    """
    access_token: str
    token_type: str


class UserLogin(BaseModel):
    """
    User login class

    Fields:
    - **email**: User email
    - **password**: User password
    """
    email: EmailStr
    password: str
