from pydantic import BaseModel


class RAMUsage(BaseModel):
    id: int
    total: float
    free: float
    used: float

    class Config:
        from_attributes = True
