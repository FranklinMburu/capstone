import uuid
from sqlalchemy import Column, String, DateTime
from datetime import datetime
from ..extensions import db

class Group(db.Model):
    __tablename__ = 'groups'

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(100), unique=True, nullable=False)
    description = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    memberships = db.relationship("GroupMembership", back_populates="group", cascade="all, delete-orphan")
    roles = db.relationship("GroupRole", back_populates="group", cascade="all, delete-orphan")
    settings = db.relationship("GroupSetting", back_populates="group", uselist=False, cascade="all, delete-orphan")
    wallet = db.relationship("GroupWallet", back_populates="group", uselist=False, cascade="all, delete-orphan")
