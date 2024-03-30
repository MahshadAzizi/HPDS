from fastapi import APIRouter, Depends
from .crud import get_ram_usage
from .schemas import RAMUsage
from typing import List
from ..config.database import get_db_session, SessionLocal

router = APIRouter(prefix="/ram")


@router.get("", response_model=List[RAMUsage])
def get_ram_usage_api(skip: int = 0, limit: int = 10, db: SessionLocal = Depends(get_db_session)):
    ram_usages = get_ram_usage(db, skip=skip, limit=limit)
    return ram_usages
