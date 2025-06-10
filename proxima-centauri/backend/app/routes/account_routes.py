from flask import Blueprint
from app.controllers.account_controller import (
    create_account_controller, get_account_controller,
    list_accounts_controller, update_account_controller,
    delete_account_controller
)

account_bp = Blueprint("account", __name__, url_prefix="/accounts")

account_bp.post("")(create_account_controller)
account_bp.get("")(list_accounts_controller)
account_bp.get("/<account_id>")(get_account_controller)
account_bp.put("/<account_id>")(update_account_controller)
account_bp.delete("/<account_id>")(delete_account_controller)
