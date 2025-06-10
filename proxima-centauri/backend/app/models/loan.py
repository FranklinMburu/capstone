import uuid
from datetime import datetime
from enum import Enum

from sqlalchemy import Column, String, DateTime, Numeric, ForeignKey, Enum as SQLEnum, Boolean
from sqlalchemy.dialects.sqlite import BLOB as SQLiteUUID
from app.extensions import db

class LoanStatus(str, Enum):
    pending = "pending"
    approved = "approved"
    rejected = "rejected"
    paid = "paid"

class Loan(db.Model):
    __tablename__ = "loans"

    id = Column(SQLiteUUID, primary_key=True, default=lambda: uuid.uuid4().bytes)
    user_id = Column(SQLiteUUID, ForeignKey("users.id"), nullable=False)
    amount = Column(Numeric(12, 2), nullable=False)
    interest_rate = Column(Numeric(4, 2), nullable=False)  # e.g., 12.50%
    term_months = Column(String(10), nullable=False)  # e.g., "12 months"
    status = Column(SQLEnum(LoanStatus, native_enum=False), default=LoanStatus.pending, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = db.relationship("User", back_populates="loans")
