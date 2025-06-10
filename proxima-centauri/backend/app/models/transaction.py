import uuid
from datetime import datetime
from enum import Enum
from sqlalchemy import Column, String, Numeric, Enum as SQLEnum, DateTime, ForeignKey
from app.extensions import db

class TransactionType(str, Enum):
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"
    SERVICE_CHARGE = "service_charge"

class PaymentMethod(str, Enum):
    MPESA = "mpesa"
    BANK = "bank"
    MANUAL = "manual"

class TransactionStatus(str, Enum):
    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"

class Transaction(db.Model):
    __tablename__ = "transactions"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    account_id = Column(String, ForeignKey("accounts.id"), nullable=False)
    type = Column(SQLEnum(TransactionType), nullable=False)
    amount = Column(Numeric(12, 2), nullable=False)
    method = Column(SQLEnum(PaymentMethod), nullable=False)
    mpesa_ref = Column(String, nullable=True)
    status = Column(SQLEnum(TransactionStatus), default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)

    user = db.relationship("User", back_populates="transactions")
    account = db.relationship("Account", back_populates="transactions")