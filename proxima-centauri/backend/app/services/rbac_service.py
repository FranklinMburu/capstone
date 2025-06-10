from app.extensions import db
from app.models.user import User
from app.models.role import Role
from app.models.permission import Permission

class RBACService:

    @staticmethod
    def assign_role_to_user(user_id: str, role_name: str) -> bool:
        user = User.query.filter_by(id=user_id).first()
        role = Role.query.filter_by(name=role_name).first()
        if not user or not role:
            return False
        if role not in user.roles:
            user.roles.append(role)
            db.session.commit()
        return True

    @staticmethod
    def remove_role_from_user(user_id: str, role_name: str) -> bool:
        user = User.query.filter_by(id=user_id).first()
        role = Role.query.filter_by(name=role_name).first()
        if not user or not role:
            return False
        if role in user.roles:
            user.roles.remove(role)
            db.session.commit()
        return True

    @staticmethod
    def assign_permission_to_role(role_name: str, permission_name: str) -> bool:
        role = Role.query.filter_by(name=role_name).first()
        permission = Permission.query.filter_by(name=permission_name).first()
        if not role or not permission:
            return False
        if permission not in role.permissions:
            role.permissions.append(permission)
            db.session.commit()
        return True

    @staticmethod
    def remove_permission_from_role(role_name: str, permission_name: str) -> bool:
        role = Role.query.filter_by(name=role_name).first()
        permission = Permission.query.filter_by(name=permission_name).first()
        if not role or not permission:
            return False
        if permission in role.permissions:
            role.permissions.remove(permission)
            db.session.commit()
        return True

    @staticmethod
    def get_roles_for_user(user_id: str):
        user = User.query.filter_by(id=user_id).first()
        if not user:
            return []
        return user.roles

    @staticmethod
    def get_permissions_for_role(role_name: str):
        role = Role.query.filter_by(name=role_name).first()
        if not role:
            return []
        return role.permissions
