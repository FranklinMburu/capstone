import uuid
from datetime import datetime
from enum import Enum

from sqlalchemy import Column, String, Enum as SQLEnum, Numeric, Boolean, DateTime, ForeignKey
from app.extensions import db

class AccountType(str, Enum):
    SAVINGS = "savings"
    CURRENT = "current"
    WALLET = "wallet"

class Account(db.Model):
    __tablename__ = "accounts"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    account_name = Column(String(100), nullable=False)
    account_type = Column(SQLEnum(AccountType), nullable=False)
    balance = Column(Numeric(12, 2), default=0.00)
    currency = Column(String(10), default="KES")
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = db.relationship("User", back_populates="accounts")
    transactions = db.relationship("Transaction", back_populates="account", cascade="all, delete-orphan")
    
