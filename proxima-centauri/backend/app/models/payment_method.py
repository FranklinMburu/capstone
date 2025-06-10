import enum
import uuid
from datetime import datetime

from sqlalchemy import Column, String, DateTime, ForeignKey, Enum as SQLEnum
from sqlalchemy.dialects.sqlite import BLOB as SQLiteUUID
from app.extensions import db

class PaymentMethodType(enum.Enum):
    card = "card"
    bank_account = "bank_account"
    mobile_money = "mobile_money"

class PaymentMethod(db.Model):
    __tablename__ = "payment_methods"

    id = Column(SQLiteUUID, primary_key=True, default=lambda: uuid.uuid4().bytes)
    user_id = Column(SQLiteUUID, ForeignKey("users.id"), nullable=False)
    type = Column(SQLEnum(PaymentMethodType, native_enum=False), nullable=False)
    provider = Column(String(50), nullable=False)
    account_number = Column(String(100), nullable=False)
    expiry_date = Column(String(7), nullable=True)  # e.g., "12/2025" for cards
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationship back to User 
    user = db.relationship("User", back_populates="payment_methods")
