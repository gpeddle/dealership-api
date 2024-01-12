from typing import List
from pydantic import BaseModel

class WorkingHours(BaseModel):
    workdays: List[str]
    workdayStartTime: str
    workdayEndTime: str
