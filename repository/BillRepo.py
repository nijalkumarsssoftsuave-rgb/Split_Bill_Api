from sqlalchemy.orm import Session
from models.BillModel import Bill


class BillRepo:
    def __init__(self, session: Session):
        self.session = session

    def create_bill(self, bill: Bill):
        self.session.add(bill)
        self.session.commit()
        self.session.refresh(bill)
        return bill

    def get_bill_by_id(self, bill_id: int):
        return self.session.query(Bill).filter(Bill.id == bill_id).first()
