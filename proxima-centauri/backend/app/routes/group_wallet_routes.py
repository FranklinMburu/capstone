from flask import Blueprint, request, jsonify
from app.schemas.group_wallet_schema import GroupWalletSchema
from app.services.group_wallet_service import create_group_wallet, get_all_group_wallets, get_group_wallet_by_id, update_group_wallet, delete_group_wallet

group_wallet_bp = Blueprint('group_wallet_bp', __name__, url_prefix='/group-wallets')
wallet_schema = GroupWalletSchema()
wallets_schema = GroupWalletSchema(many=True)

@group_wallet_bp.route('', methods=['POST'])
def create():
    data = request.get_json()
    errors = wallet_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    wallet = create_group_wallet(data)
    return wallet_schema.jsonify(wallet), 201

@group_wallet_bp.route('', methods=['GET'])
def get_all():
    wallets = get_all_group_wallets()
    return wallets_schema.jsonify(wallets), 200

@group_wallet_bp.route('/<int:wallet_id>', methods=['GET'])
def get_one(wallet_id):
    wallet = get_group_wallet_by_id(wallet_id)
    if not wallet:
        return jsonify({"message": "Wallet not found"}), 404
    return wallet_schema.jsonify(wallet), 200

@group_wallet_bp.route('/<int:wallet_id>', methods=['PUT'])
def update(wallet_id):
    wallet = get_group_wallet_by_id(wallet_id)
    if not wallet:
        return jsonify({"message": "Wallet not found"}), 404
    data = request.get_json()
    errors = wallet_schema.validate(data, partial=True)
    if errors:
        return jsonify(errors), 400
    updated_wallet = update_group_wallet(wallet, data)
    return wallet_schema.jsonify(updated_wallet), 200

@group_wallet_bp.route('/<int:wallet_id>', methods=['DELETE'])
def delete(wallet_id):
    wallet = get_group_wallet_by_id(wallet_id)
    if not wallet:
        return jsonify({"message": "Wallet not found"}), 404
    delete_group_wallet(wallet)
    return jsonify({"message": "Wallet deleted"}), 200
