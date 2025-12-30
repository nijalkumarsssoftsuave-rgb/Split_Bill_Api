from sqlalchemy.orm import Session
from models.BillPartModel import BillParticipant
from schemas.BillPartSchema import BillParticipantCreate
from .BaseRepo import BaseRespository

class BillParticipantRepo(BaseRespository):

    def create(self, data: BillParticipantCreate):
        participant = BillParticipant(**data.dict())
        self.session.add(participant)
        self.session.commit()
        self.session.refresh(participant)
        return participant

    def get_by_bill(self, bill_id: int):
        return (
            self.session.query(BillParticipant)
            .filter(BillParticipant.bill_id == bill_id)
            .all()
        )
