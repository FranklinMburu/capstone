from app.models.account import Account
from app.extensions import db

def create_account(data):
    account = Account(**data)
    db.session.add(account)
    db.session.commit()
    return account

def get_account_by_id(account_id):
    return Account.query.get(account_id)

def list_accounts():
    return Account.query.all()

def update_account(account, data):
    for key, value in data.items():
        setattr(account, key, value)
    db.session.commit()
    return account

def delete_account(account):
    db.session.delete(account)
    db.session.commit()
