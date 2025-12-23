from typing import List
from schema import BillCreate,BillResponse
from model import bills_db

def create_bill_service(bill:BillCreate):
    bill_id = len(bills_db)+1
    newBill = BillResponse(id=bill_id,**bill.model_dump())
    bills_db.append(newBill)
    return newBill

def get_bill_service(bill_id:int) -> BillResponse:
    for bill in bills_db:
        if bill.id == bill_id:
            return bill
    return None

def update_bill_service(bill_id, updated_bill):
    for i in range(len(bills_db)):
        if bills_db[i].id == bill_id:
            bills_db[i] = BillResponse(
                id=bill_id,
                title=updated_bill.title,
                total_amount=updated_bill.total_amount,
                participants=updated_bill.participants,
                paid_by=updated_bill.paid_by,
                is_setteled=updated_bill.is_setteled
            )
            return bills_db[i]
    return None


def delete_bill_service(bill_id: int):
    for bill in bills_db:
        if bill.id == bill_id:
            deletedBill = bill
            bills_db.remove(bill)
    return deletedBill

def split_bill(total_amount, participants, paid_by):
    total_people = len(participants)
    each_person_pays = total_amount / total_people
    others_owe = {}
    for person in participants:
        if person != paid_by:
            others_owe[person] = each_person_pays
    endBill = {
        "each_person_pays": each_person_pays,
        "paid_by": paid_by,
        "others_owe": others_owe
    }
    return endBill

