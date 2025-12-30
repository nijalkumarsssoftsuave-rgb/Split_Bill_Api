from repository.BillRepo import BillRepo
from models.BillModel import Bill
from schemas.BillSchema import BillCreate


class BillService:
    def __init__(self, session):
        self.repo = BillRepo(session)

    def create_bill(self, bill_data: BillCreate, user_id: int):
        bill = Bill(
            title=bill_data.title,
            total_amount=bill_data.total_amount,
            created_by=user_id
        )
        return self.repo.create_bill(bill)
