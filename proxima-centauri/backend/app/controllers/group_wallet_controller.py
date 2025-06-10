import uuid
from flask import request, jsonify
from app.extensions import db
from app.models.group_wallet import GroupWallet
from app.schemas.group_wallet_schema import GroupWalletSchema

group_wallet_schema = GroupWalletSchema()
group_wallets_schema = GroupWalletSchema(many=True)

def create_group_wallet():
    data = request.get_json()
    errors = group_wallet_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    wallet = GroupWallet(
        id=str(uuid.uuid4()),
        group_id=data['group_id'],
        balance=data.get('balance', 0.0)
    )
    db.session.add(wallet)
    db.session.commit()
    return group_wallet_schema.jsonify(wallet), 201

def get_group_wallets():
    wallets = GroupWallet.query.all()
    return group_wallets_schema.jsonify(wallets), 200

def get_group_wallet(wallet_id):
    wallet = GroupWallet.query.get(wallet_id)
    if not wallet:
        return jsonify({'message': 'Wallet not found'}), 404
    return group_wallet_schema.jsonify(wallet), 200

def update_group_wallet(wallet_id):
    wallet = GroupWallet.query.get(wallet_id)
    if not wallet:
        return jsonify({'message': 'Wallet not found'}), 404

    data = request.get_json()
    errors = group_wallet_schema.validate(data, partial=True)
    if errors:
        return jsonify(errors), 400

    if 'balance' in data:
        wallet.balance = data['balance']

    db.session.commit()
    return group_wallet_schema.jsonify(wallet), 200

def delete_group_wallet(wallet_id):
    wallet = GroupWallet.query.get(wallet_id)
    if not wallet:
        return jsonify({'message': 'Wallet not found'}), 404

    db.session.delete(wallet)
    db.session.commit()
    return jsonify({'message': 'Wallet deleted'}), 200
