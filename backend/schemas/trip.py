from pydantic import BaseModel, ConfigDict

class TripRequest(BaseModel):
    destination: str
    days: int
    budget: float

class TripResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    destination: str
    days: int
    budget: float
    category: str
    daily_budget: float