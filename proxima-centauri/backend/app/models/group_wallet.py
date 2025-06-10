import uuid
from sqlalchemy import Column, String, ForeignKey, Float
from ..extensions import db

class GroupWallet(db.Model):
    __tablename__ = 'group_wallets'

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    group_id = Column(String, ForeignKey('groups.id'), nullable=False)
    balance = Column(Float, default=0.0)

    group = db.relationship("Group", back_populates="wallet")
