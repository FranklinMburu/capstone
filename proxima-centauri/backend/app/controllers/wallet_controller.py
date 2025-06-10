from flask import request, jsonify
from app.services.wallet_service import (
    create_wallet, get_wallet_by_id, list_wallets,
    update_wallet, delete_wallet, get_wallet_by_user_id
)
from app.schemas.wallet_schema import WalletSchema

wallet_schema = WalletSchema()
wallets_schema = WalletSchema(many=True)

def create_wallet_controller():
    data = request.get_json()
    errors = wallet_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    existing = get_wallet_by_user_id(data['user_id'])
    if existing:
        return jsonify({"error": "User already has a wallet"}), 400
    wallet = create_wallet(data)
    return jsonify(wallet_schema.dump(wallet)), 201

def get_wallet_controller(wallet_id):
    wallet = get_wallet_by_id(wallet_id)
    if not wallet:
        return jsonify({"error": "Wallet not found"}), 404
    return jsonify(wallet_schema.dump(wallet))

def list_wallets_controller():
    wallets = list_wallets()
    return jsonify(wallets_schema.dump(wallets))

def update_wallet_controller(wallet_id):
    wallet = get_wallet_by_id(wallet_id)
    if not wallet:
        return jsonify({"error": "Wallet not found"}), 404
    data = request.get_json()
    wallet = update_wallet(wallet, data)
    return jsonify(wallet_schema.dump(wallet))

def delete_wallet_controller(wallet_id):
    wallet = get_wallet_by_id(wallet_id)
    if not wallet:
        return jsonify({"error": "Wallet not found"}), 404
    delete_wallet(wallet)
    return jsonify({"message": "Wallet deleted"}), 200
