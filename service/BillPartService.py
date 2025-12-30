from sqlalchemy.orm import Session
from repository.BillPartRepo import BillParticipantRepo
from schemas.BillPartSchema import BillParticipantCreate

class BillParticipantService:

    def __init__(self, session: Session):
        self.repo = BillParticipantRepo(session)

    def add_participant(self, data: BillParticipantCreate):
        return self.repo.create(data)

    def get_participants(self, bill_id: int):
        return self.repo.get_by_bill(bill_id)
