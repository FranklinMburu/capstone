from flask import request, jsonify
from app.services.transaction import (
    create_transaction, get_transaction_by_id,
    list_transactions, update_transaction, delete_transaction
)
from app.schemas.transaction import TransactionSchema

transaction_schema = TransactionSchema()
transactions_schema = TransactionSchema(many=True)

def create_transaction_controller():
    data = request.get_json()
    errors = transaction_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    transaction = create_transaction(data)
    return jsonify(transaction_schema.dump(transaction)), 201

def get_transaction_controller(transaction_id):
    transaction = get_transaction_by_id(transaction_id)
    if not transaction:
        return jsonify({"error": "Transaction not found"}), 404
    return jsonify(transaction_schema.dump(transaction))

def list_transactions_controller():
    transactions = list_transactions()
    return jsonify(transactions_schema.dump(transactions))

def update_transaction_controller(transaction_id):
    transaction = get_transaction_by_id(transaction_id)
    if not transaction:
        return jsonify({"error": "Transaction not found"}), 404
    data = request.get_json()
    transaction = update_transaction(transaction, data)
    return jsonify(transaction_schema.dump(transaction))

def delete_transaction_controller(transaction_id):
    transaction = get_transaction_by_id(transaction_id)
    if not transaction:
        return jsonify({"error": "Transaction not found"}), 404
    delete_transaction(transaction)
    return jsonify({"message": "Transaction deleted"}), 200
