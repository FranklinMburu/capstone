from app.models.admin_user import AdminUser
from app.extensions import db

def create_admin_user(data):
    admin_user = AdminUser(**data)
    db.session.add(admin_user)
    db.session.commit()
    return admin_user

def get_admin_user_by_id(admin_id):
    return AdminUser.query.get(admin_id)

def list_admin_users():
    return AdminUser.query.all()

def update_admin_user(admin_user, data):
    for key, value in data.items():
        setattr(admin_user, key, value)
    db.session.commit()
    return admin_user

def delete_admin_user(admin_user):
    db.session.delete(admin_user)
    db.session.commit()
