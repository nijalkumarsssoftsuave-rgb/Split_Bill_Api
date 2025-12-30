from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Float
from datetime import datetime, timezone
from database import Base  # your declarative base


class Bill(Base):
    __tablename__ = "bills"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    total_amount = Column(Float, nullable=False)

    created_by = Column(
        Integer,
        ForeignKey("Users.id", ondelete="CASCADE"),
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )

    is_settled = Column(Boolean, default=False)
