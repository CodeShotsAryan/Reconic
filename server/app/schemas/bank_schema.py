from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict

class BankTransactionCreate(BaseModel):
    external_id: str
    order_id: str
    amount: float
    currency: str = "INR"
    status: str
    timestamp: datetime
    extra: Optional[Dict] = None
