from typing import List, Annotated
from pydantic import BaseModel, Field
from enum import Enum


class Weekday(str, Enum):
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"


class WorkingHours(BaseModel):
    workdays: Annotated[List[Weekday],
                        Field(..., description="List of workdays")]
    workday_start_time: Annotated[str, Field(
        pattern=r'^\d{2}:\d{2}$', description="Workday start time in HH:MM format")]
    workday_end_time: Annotated[str, Field(
        pattern=r'^\d{2}:\d{2}$', description="Workday end time in HH:MM format")]


"""
# Example usage
working_hours = WorkingHours(
    workdays=[Weekday.MONDAY, Weekday.TUESDAY],
    workday_start_time='09:00',
    workday_end_time='17:00'
)
"""
