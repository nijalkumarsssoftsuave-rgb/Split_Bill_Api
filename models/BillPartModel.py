from sqlalchemy import Column, Integer, Float, Boolean, ForeignKey
from database import Base
from models.userModel import User

class BillParticipant(Base):
    __tablename__ = "bill_participants"

    id = Column(Integer, primary_key=True, index=True)

    bill_id = Column(
        Integer,
        ForeignKey("bills.id", ondelete="CASCADE"),
        nullable=False
    )

    user_id = Column(
        Integer,
        ForeignKey("Users.id", ondelete="CASCADE"),
        nullable=False
    )

    amount_paid = Column(Float, default=0.0)
    amount_owed = Column(Float, default=0.0)

    is_settled = Column(Boolean, default=False)
