from sqlalchemy import Column, Integer, String, Float, DateTime, JSON
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.core.database import Base

class GatewayTransaction(Base):
    __tablename__ = "gateway_transactions"

    id = Column(Integer, primary_key=True, index=True)
    recon_id = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, index=True)

    source = Column(String, default="GATEWAY")
    external_id = Column(String, index=True)        # PG payment_id
    order_id = Column(String, index=True)
    amount = Column(Float)
    currency = Column(String, default="INR")
    status = Column(String)
    timestamp = Column(DateTime, nullable=False)

    metadata = Column(JSON, nullable=True)

    created_at = Column(DateTime, default=func.now())
