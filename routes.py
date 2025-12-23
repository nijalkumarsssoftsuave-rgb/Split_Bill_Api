from fastapi import APIRouter,status,HTTPException
from schema import BillCreate,BillResponse
from service import create_bill_service,get_bill_service,delete_bill_service,update_bill_service,split_bill
from typing import List
from model import bills_db

router = APIRouter()

@router.post("/bills", status_code=201)
def create_bill(bill: BillCreate):
    return create_bill_service(bill)


@router.get("/bills/", response_model=List[BillResponse])
def fetch_all_bills():
    return bills_db

@router.get("/getbills/{bill_id}",response_model=BillResponse)
def get_bill(bill_id: int):
    if bill_id > len(bills_db):
        raise HTTPException(status_code=404,detail="Bill not found")
    else:
        getBill = get_bill_service(bill_id)
        return getBill

@router.put("/bills/{bill_id}")
def update_bill(bill_id: int, bill: BillCreate):
    updated = update_bill_service(bill_id, bill)
    if not updated:
        raise HTTPException(status_code=404, detail="Bill not found")
    return updated

@router.delete("/deletebills")
def delete_bill(bill_id:int):
        if bill_id > len(bills_db):
            raise HTTPException(status_code=404,detail="Bill not found")
        else:
            deleted_bill = delete_bill_service(bill_id) 
            return {"message": "Bill deleted successfully", "bill": deleted_bill}
  
    
@router.post("/bills/split")
def split_bill_api(bill: BillCreate):
    return split_bill(
        bill.total_amount,
        bill.participants,
        bill.paid_by
    )  