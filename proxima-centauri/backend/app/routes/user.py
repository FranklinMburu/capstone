from flask import Blueprint
from app.controllers.user import register_user, login_user

user_bp = Blueprint('user_bp', __name__, url_prefix='/api/users')

user_bp.route('/register', methods=['POST'])(register_user)
user_bp.route('/login', methods=['POST'])(login_user)
