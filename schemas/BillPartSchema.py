from pydantic import BaseModel

class BillParticipantCreate(BaseModel):
    bill_id: int
    user_id: int
    amount_paid: float
    amount_owed: float

class BillParticipantResponse(BillParticipantCreate):
    id: int
    is_settled: bool

    class Config:
        from_attributes = True
