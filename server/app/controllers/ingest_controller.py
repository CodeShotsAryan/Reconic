from sqlalchemy.orm import Session
from app.models.bank_model import BankTransaction
from app.models.gateway_model import GatewayTransaction
from app.models.merchant_model import MerchantTransaction
from app.schemas.bank_schema import BankTransactionCreate
from app.schemas.gateway_schema import GatewayTransactionCreate
from app.schemas.merchant_schema import MerchantTransactionCreate


def ingest_bank(db: Session, data: BankTransactionCreate):
    entry = BankTransaction(**data.dict())
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry


def ingest_gateway(db: Session, data: GatewayTransactionCreate):
    entry = GatewayTransaction(**data.dict())
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry


def ingest_merchant(db: Session, data: MerchantTransactionCreate):
    entry = MerchantTransaction(**data.dict())
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry
