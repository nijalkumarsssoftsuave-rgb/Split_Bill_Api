from fastapi import APIRouter,Depends
from service.UserService import UserService
from schemas.userSchema import UserInLogin,UserOutput,UserCreate,UserWithToken
from sqlalchemy.orm import Session
from database import get_db
from utils.security import get_current_user

authRouter = APIRouter()

@authRouter.post("/login",status_code=200,response_model=UserWithToken)
def login(user_login:UserInLogin,session:Session = Depends(get_db)):
    try:
        return UserService(session=session).user_login(user_detail=user_login)
    except Exception as error:
        print(error)
        raise error
    

@authRouter.post("/signup",status_code=201,response_model=UserOutput)
def signup(user_signup:UserCreate,session:Session = Depends(get_db)):
    try:
        return UserService(session=session).user_signup(user_details=user_signup)
    except Exception as error:
        print(error)
        raise error
    
@authRouter.get("/me", response_model=UserOutput)
def get_me(
    current_user = Depends(get_current_user),
    session: Session = Depends(get_db)
):
    return UserService(session).get_current_user(current_user.id)