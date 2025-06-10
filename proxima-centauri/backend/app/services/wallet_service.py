from app.models.wallet import Wallet
from app.extensions import db

def create_wallet(data):
    wallet = Wallet(**data)
    db.session.add(wallet)
    db.session.commit()
    return wallet

def get_wallet_by_id(wallet_id):
    return Wallet.query.get(wallet_id)

def get_wallet_by_user_id(user_id):
    return Wallet.query.filter_by(user_id=user_id).first()

def list_wallets():
    return Wallet.query.all()

def update_wallet(wallet, data):
    for key, value in data.items():
        setattr(wallet, key, value)
    db.session.commit()
    return wallet

def delete_wallet(wallet):
    db.session.delete(wallet)
    db.session.commit()
