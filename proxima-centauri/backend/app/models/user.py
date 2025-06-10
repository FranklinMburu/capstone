import uuid
from datetime import datetime
from sqlalchemy import Column, String, Boolean, DateTime
from werkzeug.security import generate_password_hash, check_password_hash
from ..extensions import db
from app.models.user_role import user_roles
from app.models.role import Role
from app.models.permission import Permission
from app.models.group_membership import GroupMembership


class User(db.Model):
    __tablename__ = 'users'

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    full_name = Column(String(100), nullable=False)
    phone_number = Column(String(15), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=True)
    password_hash = Column(String(128), nullable=False)
    is_verified = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    accounts = db.relationship("Account", back_populates="user", cascade="all, delete-orphan")
    transactions = db.relationship("Transaction", back_populates="user", cascade="all, delete-orphan")
    payment_methods = db.relationship("PaymentMethod", back_populates="user", cascade="all, delete-orphan")
    wallets = db.relationship("Wallet", back_populates="user", cascade="all, delete-orphan")
    investments = db.relationship("Investment", back_populates="user", cascade="all, delete-orphan")
    loans = db.relationship("Loan", back_populates="user", cascade="all, delete-orphan")
    notifications = db.relationship("Notification", back_populates="user", cascade="all, delete-orphan")
    group_memberships = db.relationship("GroupMembership", back_populates="user", cascade="all, delete-orphan")


    # ✅ Many-to-many relationship with roles
    roles = db.relationship("Role", secondary=user_roles, backref="users")

    # Password hashing methods
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.full_name}>"
