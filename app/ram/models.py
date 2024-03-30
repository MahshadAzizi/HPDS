from sqlalchemy import Column, Integer, DECIMAL
from app.config.database import Base


class RAMUsage(Base):
    __tablename__ = "ram_usage"

    id = Column(Integer, primary_key=True, index=True)
    total = Column(DECIMAL(10, 2))  # Adjust precision and scale as needed
    free = Column(DECIMAL(10, 2))
    used = Column(DECIMAL(10, 2))