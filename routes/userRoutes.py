from fastapi import APIRouter,Depends
from service.UserService import UserService
from schemas.userSchema import UserInLogin,UserOutput,UserCreate,UserWithToken,UsageStatsOut
from sqlalchemy.orm import Session
from database import get_db
from utils.security import get_current_user
from dependencies.rate_limit import rate_limiter
from repository.userRepo import UserRepository
from models.userModel import User
from models.apiUsageModel import APIUsage
from sqlalchemy import func


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
    
@authRouter.get("/me", 
                response_model=UserOutput,
                dependencies=[Depends(rate_limiter)])
def get_me(current_user: User = Depends(get_current_user)):
    return current_user

@authRouter.get("/usage-stats")
def get_usage_stats(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    stats = (
        db.query(
            APIUsage.endpoint,
            APIUsage.method,
            func.count(APIUsage.id).label("total_hits"),
        )
        .filter(APIUsage.user_id == current_user.id)
        .group_by(APIUsage.endpoint, APIUsage.method)
        .all()
    )

    return [
        {
            "endpoint": s.endpoint,
            "method": s.method,
            "total_hits": s.total_hits,
        }
        for s in stats
    ]
