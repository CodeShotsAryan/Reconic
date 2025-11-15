from sqlalchemy import Column, Integer, String, Float, DateTime, JSON
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.core.database import Base

class BankTransaction(Base):
    __tablename__ = "bank_transactions"

    id = Column(Integer, primary_key=True, index=True)
    recon_id = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, index=True)

    source = Column(String, default="BANK")
    external_id = Column(String, index=True)        # Bank reference number
    order_id = Column(String, index=True)
    amount = Column(Float)
    currency = Column(String, default="INR")
    status = Column(String)
    timestamp = Column(DateTime, nullable=False)
    extra = Column(JSON, nullable=True)

    created_at = Column(DateTime, default=func.now())
