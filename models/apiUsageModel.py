from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from database import Base

class APIUsage(Base):
    __tablename__ = "api_usage"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("Users.id"))
    endpoint = Column(String, nullable=False)
    method = Column(String, nullable=False)
    timestamp = Column(
    DateTime(timezone=True),
    server_default=func.now(),
    nullable=False
)
