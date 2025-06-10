from flask import Blueprint
from app.controllers.loan import (
    create_loan_controller, get_loan_controller,
    list_loans_controller, update_loan_controller,
    delete_loan_controller
)

loan_bp = Blueprint("loan", __name__, url_prefix="/loans")

loan_bp.post("")(create_loan_controller)
loan_bp.get("")(list_loans_controller)
loan_bp.get("/<loan_id>")(get_loan_controller)
loan_bp.put("/<loan_id>")(update_loan_controller)
loan_bp.delete("/<loan_id>")(delete_loan_controller)
