from flask import request, jsonify
from app.services.account_service import (
    create_account, get_account_by_id, list_accounts,
    update_account, delete_account
)
from app.schemas.account_schema import AccountSchema

account_schema = AccountSchema()
accounts_schema = AccountSchema(many=True)

def create_account_controller():
    data = request.get_json()
    errors = account_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    account = create_account(data)
    return jsonify(account_schema.dump(account)), 201

def get_account_controller(account_id):
    account = get_account_by_id(account_id)
    if not account:
        return jsonify({"error": "Account not found"}), 404
    return jsonify(account_schema.dump(account)), 200

def list_accounts_controller():
    accounts = list_accounts()
    return jsonify(accounts_schema.dump(accounts)), 200

def update_account_controller(account_id):
    account = get_account_by_id(account_id)
    if not account:
        return jsonify({"error": "Account not found"}), 404
    data = request.get_json()
    account = update_account(account, data)
    return jsonify(account_schema.dump(account)), 200

def delete_account_controller(account_id):
    account = get_account_by_id(account_id)
    if not account:
        return jsonify({"error": "Account not found"}), 404
    delete_account(account)
    return jsonify({"message": "Account deleted"}), 200
