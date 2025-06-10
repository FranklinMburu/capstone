import uuid
from sqlalchemy import Column, String, ForeignKey
from ..extensions import db

class GroupRole(db.Model):
    __tablename__ = 'group_roles'

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    group_id = Column(String, ForeignKey('groups.id'), nullable=False)
    name = Column(String(50), nullable=False)
    description = Column(String(255), nullable=True)

    group = db.relationship("Group", back_populates="roles")
