from app.models.transaction import Transaction
from app.extensions import db

def create_transaction(data):
    transaction = Transaction(**data)
    db.session.add(transaction)
    db.session.commit()
    return transaction

def get_transaction_by_id(transaction_id):
    return Transaction.query.get(transaction_id)

def list_transactions():
    return Transaction.query.all()

def update_transaction(transaction, data):
    for key, value in data.items():
        setattr(transaction, key, value)
    db.session.commit()
    return transaction

def delete_transaction(transaction):
    db.session.delete(transaction)
    db.session.commit()
