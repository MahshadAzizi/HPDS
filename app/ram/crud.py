from sqlalchemy.orm import Session
from app.ram.models import RAMUsage


def create_ram_usage(db: Session, total: float, free: float, used: float):
    db_ram_usage = RAMUsage(total=total, free=free, used=used)
    db.add(db_ram_usage)
    db.commit()
    db.refresh(db_ram_usage)
    return db_ram_usage


def get_ram_usage(db: Session, skip: int = 0, limit: int = 10):
    return db.query(RAMUsage).offset(skip).limit(limit).all()


def get_ram_usage_count(db: Session):
    return db.query(RAMUsage).count()
