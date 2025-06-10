from flask import Blueprint
from app.controllers.transaction import (
    create_transaction_controller, get_transaction_controller,
    list_transactions_controller, update_transaction_controller,
    delete_transaction_controller
)

transaction_bp = Blueprint("transaction", __name__, url_prefix="/transactions")

transaction_bp.post("")(create_transaction_controller)
transaction_bp.get("")(list_transactions_controller)
transaction_bp.get("/<transaction_id>")(get_transaction_controller)
transaction_bp.put("/<transaction_id>")(update_transaction_controller)
transaction_bp.delete("/<transaction_id>")(delete_transaction_controller)
