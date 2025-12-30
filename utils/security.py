from bcrypt import checkpw, hashpw, gensalt
import jwt
import time

from decouple import config
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from database import get_db
from models.userModel import User


JWT_SECRET = config("JWT_SECRET")
JWT_ALGORITHM = config("JWT_ALGORITHM")

security = HTTPBearer()



class AuthHelper(object):

    @staticmethod
    def sign_jwt(user_id: int) -> str:
        """
        Create JWT token
        """
        payload = {
            "user_id": user_id,
            "exp": int(time.time()) + 900 
        }

        token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
        return token

    @staticmethod
    def decode_jwt(token: str) -> dict | None:
        """
        Decode JWT token
        """
        try:
            decoded_token = jwt.decode(
                token,
                JWT_SECRET,
                algorithms=[JWT_ALGORITHM]
            )
            return decoded_token

        except jwt.ExpiredSignatureError:
            print("JWT ERROR: Token expired")
            return None

        except jwt.InvalidTokenError as e:
            print("JWT ERROR:", e)
            return None




class hashingPass(object):

    @staticmethod
    def hash_password(password: str) -> str:
        return hashpw(
            password.encode("utf-8"),
            gensalt()
        ).decode("utf-8")

    @staticmethod
    def verify_password(password: str, hashed_pass: str) -> bool:
        return checkpw(
            password.encode("utf-8"),
            hashed_pass.encode("utf-8")
        )


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    session: Session = Depends(get_db)
):
    """
    Dependency to get logged-in user from JWT
    """
    token = credentials.credentials

    payload = AuthHelper.decode_jwt(token)

    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )

    user_id = payload.get("user_id")
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token payload"
        )

    user = session.query(User).filter(User.id == user_id).first()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )

    return user