from repository.userRepo import UserRepository
from schemas.userSchema import UserInLogin,UserCreate,UserOutput,UserWithToken
from utils.security import AuthHelper,hashingPass
from sqlalchemy.orm import Session
from fastapi import HTTPException


class UserService:
    def __init__(self,session:Session):
        self.__userRepostiory = UserRepository(session=session)
    
    def user_signup(self,user_details:UserCreate) -> UserOutput:

        if self.__userRepostiory.user_exist_by_email(email=user_details.email):
            raise HTTPException(status_code=400,detail="User already found Please login")
        
        hashedPass = hashingPass.hash_password(password=user_details.hashed_password)
        user_details.hashed_password = hashedPass
        return self.__userRepostiory.create_user(user_data=user_details)
    
    def user_login(self,user_detail:UserInLogin) ->UserWithToken:

        if not self.__userRepostiory.user_exist_by_email(email=user_detail.email):
            raise HTTPException(status_code=400,detail="User Not Available")
        
        user = self.__userRepostiory.get_user_by_email(email=user_detail.email)
        if hashingPass.verify_password(password=user_detail.hashed_password,hashed_pass=user.hashed_password):
            token = AuthHelper.sign_jwt(user_id = user.id)
            if token:
                return UserWithToken(token= token)
            raise HTTPException(status_code=500,detail="Invalid token")
        raise HTTPException(status_code=400,detail="Password mismatched")
    
    