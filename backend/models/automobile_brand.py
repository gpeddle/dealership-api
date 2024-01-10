from pydantic import BaseModel

class AutomobileBrand(BaseModel):
    id: int
    brand: str
    markupPercentage: int
