import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.sqlite import BLOB as SQLiteUUID
from sqlalchemy.orm import relationship
from app.extensions import db
from app.models.role_permission import role_permissions  #  Import only

class Permission(db.Model):
    __tablename__ = "permissions"

    id = Column(SQLiteUUID, primary_key=True, default=lambda: uuid.uuid4().bytes)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)

    roles = relationship("Role", secondary=role_permissions, back_populates="permissions")
