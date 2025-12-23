from typing import List
from pydantic import BaseModel,field_validator


class BillCreate(BaseModel):
    title:str
    total_amount:int
    participants:List[str]
    paid_by:str
    is_setteled:bool
    

    @field_validator("total_amount")
    @classmethod
    def total_amount_validation(cls, value):
        if value <= 0:
            raise ValueError("Total amount must be greater than zero")
        return value

    @field_validator("paid_by")
    @classmethod
    def paid_in_participants(cls, val, inf0):
        participants = inf0.data.get("participants")
        if participants and val not in participants:
            raise ValueError("Paid_by must be one of the participants")
        return val
    
class BillResponse(BillCreate):
    id:int