from pydantic import BaseModel, Field
from typing import List


class KeyDevelopment(BaseModel):
    date: str = Field(
        ..., description="The date of the event. Use ISO 8601 format (YYYY-MM-DD) or just year if no exact day/month."
    )
    description: str = Field(
        ..., description="A concise description of the historical event."
    )
    evidence: str = Field(
        ..., description="The exact sentence(s) from the text that supports this event."
    )


class ExtractionData(BaseModel):
    key_developments: List[KeyDevelopment]