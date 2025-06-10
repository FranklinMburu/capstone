from flask import request, jsonify
from app.services.investment_service import (
    create_investment, get_investment_by_id,
    list_investments, update_investment,
    delete_investment
)
from app.schemas.investment_schema import InvestmentSchema

investment_schema = InvestmentSchema()
investments_schema = InvestmentSchema(many=True)

def create_investment_controller():
    data = request.get_json()
    errors = investment_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    investment = create_investment(data)
    return jsonify(investment_schema.dump(investment)), 201  # fixed here

def get_investment_controller(investment_id):
    investment = get_investment_by_id(investment_id)
    if not investment:
        return jsonify({"error": "Investment not found"}), 404
    return jsonify(investment_schema.dump(investment))  # fixed here

def list_investments_controller():
    investments = list_investments()
    return jsonify(investments_schema.dump(investments))  # already correct

def update_investment_controller(investment_id):
    investment = get_investment_by_id(investment_id)
    if not investment:
        return jsonify({"error": "Investment not found"}), 404
    data = request.get_json()
    investment = update_investment(investment, data)
    return jsonify(investment_schema.dump(investment))  # fixed here

def delete_investment_controller(investment_id):
    investment = get_investment_by_id(investment_id)
    if not investment:
        return jsonify({"error": "Investment not found"}), 404
    delete_investment(investment)
    return jsonify({"message": "Investment deleted"}), 200
