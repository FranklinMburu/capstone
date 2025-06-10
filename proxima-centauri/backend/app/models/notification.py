import uuid
from datetime import datetime
from enum import Enum

from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, Enum as SQLEnum
from sqlalchemy.dialects.sqlite import BLOB as SQLiteUUID
from app.extensions import db

class NotificationType(str, Enum):
    REMINDER = "reminder"
    ALERT = "alert"
    SYSTEM = "system"

class Notification(db.Model):
    __tablename__ = "notifications"

    id = Column(SQLiteUUID, primary_key=True, default=lambda: uuid.uuid4().bytes)
    user_id = Column(SQLiteUUID, ForeignKey("users.id"), nullable=False)
    message = Column(String, nullable=False)
    type = Column(SQLEnum(NotificationType), nullable=False)
    scheduled_time = Column(DateTime, nullable=True)
    sent = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    user = db.relationship("User", back_populates="notifications")