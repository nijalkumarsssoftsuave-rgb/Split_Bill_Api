from sqlalchemy.orm import Session
from models.BillModel import Bill
from .BaseRepo import BaseRespository

class BillRepo(BaseRespository):
    
    def create_bill(self, bill: Bill):
        self.session.add(bill)
        self.session.commit()
        self.session.refresh(bill)
        return bill

    def get_bill_by_id(self, bill_id: int):
        return self.session.query(Bill).filter(Bill.id == bill_id).first()
