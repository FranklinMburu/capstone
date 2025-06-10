from flask import Blueprint
from app.controllers.investment_controller import (
    create_investment_controller, get_investment_controller,
    list_investments_controller, update_investment_controller,
    delete_investment_controller
)

investment_bp = Blueprint("investment", __name__, url_prefix="/investments")

investment_bp.post("")(create_investment_controller)
investment_bp.get("")(list_investments_controller)
investment_bp.get("/<investment_id>")(get_investment_controller)
investment_bp.put("/<investment_id>")(update_investment_controller)
investment_bp.delete("/<investment_id>")(delete_investment_controller)
