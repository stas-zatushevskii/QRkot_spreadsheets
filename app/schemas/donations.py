from datetime import datetime, timedelta
from http import HTTPStatus
from typing import Optional

from fastapi import HTTPException
from pydantic import BaseModel, Field, validator


MIN_VALUE = 0
MINUTES = 10
HOURS = 1


CREATED_TIME = (
    datetime.now() + timedelta(minutes=MINUTES)
).isoformat(timespec='minutes')

CLOSED_TIME = (
    datetime.now() + timedelta(hours=HOURS)
).isoformat(timespec='minutes')


class DonationsBase(BaseModel):
    comment: Optional[str] = Field(None, min_length=1)
    full_amount: Optional[int] = Field(0)
    invested_amount: Optional[int] = Field(0)
    fully_invested: Optional[bool] = Field(False)
    create_date: Optional[datetime] = Field(None)
    close_date: Optional[datetime] = Field(None)


class DonationsCreate(DonationsBase):
    full_amount: int

    @validator('full_amount')
    def int_validator(cls, value: int):
        if value <= MIN_VALUE:
            raise HTTPException(
                status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
            )
        return value


class DonationsDB(DonationsBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
