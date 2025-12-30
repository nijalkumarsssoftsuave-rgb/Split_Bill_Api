from sqlalchemy.orm import Session

class BaseRespository:
    def __init__(self,session:Session) -> None:
        self.session = session