from .BaseRepo import BaseRespository
from schemas.userSchema import UserCreate,UserOutput
from models.userModel import User
from models.apiUsageModel import APIUsage
from sqlalchemy import func
class UserRepository(BaseRespository):

    def create_user(self,user_data:UserCreate):
        
        newUser = User(**user_data.model_dump(exclude_none=True))

        self.session.add(instance= newUser)
        self.session.commit()
        self.session.refresh(instance= newUser)
        return newUser
    
    def user_exist_by_email(self,email : str) -> bool:
        user = self.session.query(User).filter_by(email=email).first()
        return bool(user)
    
    def get_user_by_email(self,email:str) -> User:
        user = self.session.query(User).filter_by(email=email).first()
        return user 
    
    def get_user_by_id(self,user_id:int) -> User:
        user = self.session.query(User).filter_by(id = user_id).first()
        return user
    
    def get_user_api_stats(session, user_id: int):
        return session.query(
            APIUsage.endpoint,
            APIUsage.method,
            func.count(APIUsage.id).label("count")
        ).filter(
            APIUsage.user_id == user_id
        ).group_by(
            APIUsage.endpoint,
            APIUsage.method
        ).all()
