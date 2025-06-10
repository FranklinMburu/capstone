from flask import Blueprint
from app.controllers.wallet_controller import (
    create_wallet_controller, get_wallet_controller,
    list_wallets_controller, update_wallet_controller,
    delete_wallet_controller
)

wallet_bp = Blueprint("wallet", __name__, url_prefix="/wallets")

wallet_bp.post("")(create_wallet_controller)
wallet_bp.get("")(list_wallets_controller)
wallet_bp.get("/<wallet_id>")(get_wallet_controller)
wallet_bp.put("/<wallet_id>")(update_wallet_controller)
wallet_bp.delete("/<wallet_id>")(delete_wallet_controller)
