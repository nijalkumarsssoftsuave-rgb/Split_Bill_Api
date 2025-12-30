from pydantic import BaseModel
from datetime import datetime


class BillCreate(BaseModel):
    title: str
    total_amount: float


class BillOut(BaseModel):
    id: int
    title: str
    total_amount: float
    created_by: int
    created_at: datetime
    is_settled: bool

    class Config:
        from_attributes = True  # pydantic v2
