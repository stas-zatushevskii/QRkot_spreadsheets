from datetime import datetime, timedelta
from typing import Optional

from pydantic import BaseModel, Extra, Field, PositiveInt


MAX_VALUE = 100
MIN_VALUE = 1
MINUTES = 10
HOURS = 1
TEST_DATA = 500


CREATED_TIME = (
    datetime.now() + timedelta(minutes=MINUTES)
).isoformat(timespec='minutes')

CLOSED_TIME = (
    datetime.now() + timedelta(hours=HOURS)
).isoformat(timespec='minutes')


class ProjectsCreate(BaseModel):
    name: str = Field(..., min_length=MIN_VALUE, max_length=MAX_VALUE)
    description: str = Field(..., min_length=MIN_VALUE)
    full_amount: PositiveInt

    class Config:
        # Выкинет ошибку когда какое-либо дополнительное поле попадет в схему
        extra = Extra.forbid
        schema_extra = {
            'example': {
                'name': 'Мощный котик',
                'description': 'Создаем фитнесс-центр',
                'full_amount': TEST_DATA
            }
        }


class ProjectsUpdate(BaseModel):

    name: Optional[str] = Field(min_length=MIN_VALUE, max_length=MAX_VALUE)
    description: Optional[str] = Field(min_length=MIN_VALUE)
    full_amount: Optional[PositiveInt]

    class Config:
        # Выкинет ошибку когда какое-либо дополнительное поле попадет в схему
        extra = Extra.forbid
        schema_extra = {
            'example': {
                'name': 'Мощный котик',
                'description': 'Создаем фитнесс-центр',
                'full_amount': TEST_DATA
            }
        }


class ProjectsDB(ProjectsCreate):
    id: int
    invested_amount: int
    fully_invested: bool
    create_date: datetime
    close_date: Optional[datetime]

    class Config:
        orm_mode = True
