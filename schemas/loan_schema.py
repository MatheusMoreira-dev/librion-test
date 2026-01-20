from pydantic import BaseModel
from schemas.copy_schema import CopyResponse
from datetime import datetime

class LoanRequest(BaseModel):
    copy_id:int

    class Config:
        from_attributes = True

class LoanResponse(BaseModel):
    id: int
    reader_id: int
    copy_data: CopyResponse
    request_date: datetime
    taken_date: datetime | None
    return_date: datetime
    active: bool

    class Config:
        from_attributes = True
