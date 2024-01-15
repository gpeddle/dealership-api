from pydantic import BaseModel, Field
from pydantic.types import Annotated


class AutomobileBrand(BaseModel):
    id: int = Field(...,
                    description="Unique identifier for the automobile brand")
    brand: str = Field(..., description="Name of the automobile brand")
    markupPercentage: Annotated[int,
                                Field(..., description="Markup percentage", ge=0, le=100)]

"""
# Example usage
brand_example = AutomobileBrand(
    id=1,
    brand="Ford",
    markupPercentage=12
)
"""