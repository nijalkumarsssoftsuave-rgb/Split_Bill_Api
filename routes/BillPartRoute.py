from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from utils.security import get_current_user
from service.BillPartService import BillParticipantService
from schemas.BillPartSchema import (
    BillParticipantCreate,
    BillParticipantResponse
)

router = APIRouter(
    prefix="/bill-participants",
    tags=["Bill Participants"]
)

@router.post(
    "/",
    response_model=BillParticipantResponse
)
def add_participant(
    data: BillParticipantCreate,
    session: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return BillParticipantService(session).add_participant(data)


@router.get(
    "/bill/{bill_id}",
    response_model=list[BillParticipantResponse]
)
def get_bill_participants(
    bill_id: int,
    session: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return BillParticipantService(session).get_participants(bill_id)
