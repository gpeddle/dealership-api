from typing import List
from pydantic import BaseModel

class ServiceBay(BaseModel):
    id: int
    name: str
    equipment: List[str]