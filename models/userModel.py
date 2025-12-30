from database import Base 
from sqlalchemy import Integer,Column,String,DateTime
from datetime import datetime,timezone


class User(Base):
    
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String(100))
    hashed_password = Column(String(255))
    created_at = Column(DateTime(timezone=True),
                        default=lambda: datetime.now(timezone.utc),
                        onupdate=lambda: datetime.now(timezone.utc))
 