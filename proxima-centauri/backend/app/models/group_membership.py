import uuid
from sqlalchemy import Column, String, ForeignKey, DateTime
from datetime import datetime
from ..extensions import db

class GroupMembership(db.Model):
    __tablename__ = 'group_memberships'

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey('users.id'), nullable=False)
    group_id = Column(String, ForeignKey('groups.id'), nullable=False)
    joined_at = Column(DateTime, default=datetime.utcnow)

    group = db.relationship("Group", back_populates="memberships")
    user = db.relationship("User", back_populates="group_memberships")
