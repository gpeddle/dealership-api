from typing import List
from pydantic import BaseModel, Field

class ServiceBay(BaseModel):
    id: int = Field(..., description="Unique identifier for the service bay")
    name: str = Field(..., description="Name of the service bay")
    equipment: List[str] = Field(..., description="List of equipment available in the service bay")

# Example usage
service_bay_example = ServiceBay(
    id=1,
    name="Service Bay 1",
    equipment=["Lift", "Diagnostic Tools", "Tire Changer"]
)
