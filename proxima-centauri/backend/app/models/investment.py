import uuid
from datetime import datetime
from enum import Enum
from sqlalchemy import Column, String, Numeric, DateTime, ForeignKey, Enum as SQLEnum
from sqlalchemy.dialects.sqlite import BLOB as SQLiteUUID
from app.extensions import db

class InvestmentType(str, Enum):
    STOCKS = "stocks"
    BONDS = "bonds"
    FUND = "fund"

class Investment(db.Model):
    __tablename__ = "investments"

    id = Column(SQLiteUUID, primary_key=True, default=lambda: uuid.uuid4().bytes)
    user_id = Column(SQLiteUUID, ForeignKey("users.id"), nullable=False)
    type = Column(SQLEnum(InvestmentType), nullable=False)
    amount = Column(Numeric(12, 2), nullable=False)
    returns = Column(Numeric(12, 2), default=0.00)
    description = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    user = db.relationship("User", back_populates="investments")