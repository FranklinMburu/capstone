import uuid
from sqlalchemy import Column, String, ForeignKey, Integer
from ..extensions import db

class GroupSetting(db.Model):
    __tablename__ = 'group_settings'

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    group_id = Column(String, ForeignKey('groups.id'), nullable=False, unique=True)
    min_signatories = Column(Integer, default=1)
    rules = Column(String(500), nullable=True)

    group = db.relationship("Group", back_populates="settings")
