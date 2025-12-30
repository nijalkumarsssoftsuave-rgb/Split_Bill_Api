from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from service.BillService import BillService
from schemas.BillSchema import BillCreate, BillOut
from database import get_db
from utils.security import get_current_user
Billrouter = APIRouter()


@Billrouter.post("/bills", response_model=BillOut)
def create_bill(
    bill: BillCreate,
    session: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return BillService(session).create_bill(
        bill_data=bill,
        user_id=current_user.id
    )
