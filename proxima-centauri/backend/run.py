from flask import Flask
from app.extensions import db, jwt
from app.routes.user import user_bp
from app.routes.account_routes import account_bp
from app.routes.transaction import transaction_bp
from app.routes.wallet_routes import wallet_bp
from app.routes.payment_method import payment_method_bp
from app.routes.investment_routes import investment_bp
from app.routes.notification import notification_bp
from app.routes.admin_user_routes import admin_user_bp
from app.routes.role_routes import role_bp
from app.routes.permission_routes import permission_bp
from app.routes.loan import loan_bp
from app.routes.auth_routes import auth_bp
from app.routes.group_routes import group_bp
from app.routes.group_membership_routes import group_membership_bp
from app.routes.group_role_routes import group_role_bp
from app.routes.group_wallet_routes import group_wallet_bp
from app.routes.group_setting_routes import group_setting_bp

# ✅ Import Flasgger
from flasgger import Swagger
from flasgger.utils import swag_from

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('instance/config.py')

    # JWT config
    app.config["JWT_SECRET_KEY"] = app.config.get("JWT_SECRET_KEY", "super-secret-key")

    # ✅ Flasgger config (optional title/info)
    app.config['SWAGGER'] = {
        'title': 'Proxima Centauri API',
        'uiversion': 3
    }

    # Init extensions
    db.init_app(app)
    jwt.init_app(app)
    swagger = Swagger(app)  # ✅ Initialize Swagger

    with app.app_context():
        db.create_all()

    @app.route('/')
    def index():
        return {"message": "Proxima Centauri API is running."}

    # Register blueprints
    app.register_blueprint(user_bp)
    app.register_blueprint(account_bp)
    app.register_blueprint(transaction_bp)
    app.register_blueprint(wallet_bp)
    app.register_blueprint(payment_method_bp)
    app.register_blueprint(investment_bp)
    app.register_blueprint(notification_bp)
    app.register_blueprint(admin_user_bp)
    app.register_blueprint(role_bp)
    app.register_blueprint(permission_bp)
    app.register_blueprint(loan_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(group_bp)
    app.register_blueprint(group_membership_bp)
    app.register_blueprint(group_role_bp)
    app.register_blueprint(group_wallet_bp)
    app.register_blueprint(group_setting_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
