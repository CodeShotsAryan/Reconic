from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.bank_schema import BankTransactionCreate
from app.schemas.gateway_schema import GatewayTransactionCreate
from app.schemas.merchant_schema import MerchantTransactionCreate

from app.controllers.ingest_controller import (
    ingest_bank,
    ingest_gateway,
    ingest_merchant
)

router = APIRouter(prefix="/ingest", tags=["Ingestion"])


@router.post("/bank")
def ingest_bank_route(payload: BankTransactionCreate, db: Session = Depends(get_db)):
    return ingest_bank(db, payload)


@router.post("/gateway")
def ingest_gateway_route(payload: GatewayTransactionCreate, db: Session = Depends(get_db)):
    return ingest_gateway(db, payload)


@router.post("/merchant")
def ingest_merchant_route(payload: MerchantTransactionCreate, db: Session = Depends(get_db)):
    return ingest_merchant(db, payload)
