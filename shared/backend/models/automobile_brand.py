from pydantic import BaseModel, Field, conint
from pydantic.types import Annotated


class AutomobileBrand(BaseModel):
    id: int = Field(...,
                    description="Unique identifier for the automobile brand")
    brand: str = Field(..., description="Name of the automobile brand")
    markupPercentage: Annotated[int,
                                Field(..., description="Markup percentage", ge=0, le=100)]
