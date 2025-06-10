from app.extensions import db
from app.models.group_wallet import GroupWallet

def create_group_wallet(data):
    wallet = GroupWallet(**data)
    db.session.add(wallet)
    db.session.commit()
    return wallet

def get_all_group_wallets():
    return GroupWallet.query.all()

def get_group_wallet_by_id(wallet_id):
    return GroupWallet.query.get(wallet_id)

def update_group_wallet(wallet, data):
    for key, value in data.items():
        setattr(wallet, key, value)
    db.session.commit()
    return wallet

def delete_group_wallet(wallet):
    db.session.delete(wallet)
    db.session.commit()
