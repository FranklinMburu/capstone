import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.sqlite import BLOB as SQLiteUUID
from sqlalchemy.orm import relationship
from app.extensions import db
from app.models.role_permission import role_permissions

class Role(db.Model):
    __tablename__ = "roles"

    id = Column(SQLiteUUID, primary_key=True, default=lambda: uuid.uuid4().bytes)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)

    permissions = relationship("Permission", secondary=role_permissions, back_populates="roles")
