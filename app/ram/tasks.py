from celery import shared_task
import psutil

from app.config.database import SessionLocal
from app.ram.crud import create_ram_usage


@shared_task
def ram_usage_collector():
    import time
    time.sleep(5)
    ram = psutil.virtual_memory()
    total = ram.total // (1024 * 1024)  # Convert to MB
    free = ram.available // (1024 * 1024)
    used = ram.used // (1024 * 1024)
    db = SessionLocal()
    create_ram_usage(db, total=total, free=free, used=used)
    db.close()
    return total, free, used
