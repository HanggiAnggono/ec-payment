from enum import Enum
from uuid import uuid4
from sqlmodel import Field, SQLModel


class TransactionStatus(str, Enum):
    SETTLEMENT = "settlement"
    PENDING = "pending"
    FAILURE = "failure"

class Payment(SQLModel, table=True):
  id: str = Field(default=uuid4(), primary_key=True)
  status: TransactionStatus = Field(default=TransactionStatus.PENDING)
  gross_amount: float
  currency: str
  order_id: str
  payment_type: str
  signature_key: str
  transaction_id: str
  transaction_status: TransactionStatus
  fraud_status: str
  status_message: str
  merchant_id: str
  transaction_type: str
  issuer: str
  acquirer: str
  transaction_time: str
  settlement_time: str
  expiry_time: str