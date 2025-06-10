from flask import request, jsonify
from app.schemas.loan import LoanSchema
from app.services.loan import create_loan, get_loan_by_id, list_loans, update_loan, delete_loan

loan_schema = LoanSchema()
loans_schema = LoanSchema(many=True)

def create_loan_controller():
    data = request.get_json()
    errors = loan_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    loan = create_loan(data)
    return jsonify(loan_schema.dump(loan)), 201

def get_loan_controller(loan_id):
    loan = get_loan_by_id(loan_id)
    if not loan:
        return jsonify({"error": "Loan not found"}), 404
    return jsonify(loan_schema.dump(loan))

def list_loans_controller():
    loans = list_loans()
    return jsonify(loans_schema.dump(loans))

def update_loan_controller(loan_id):
    loan = get_loan_by_id(loan_id)
    if not loan:
        return jsonify({"error": "Loan not found"}), 404
    data = request.get_json()
    loan = update_loan(loan, data)
    return jsonify(loan_schema.dump(loan))

def delete_loan_controller(loan_id):
    loan = get_loan_by_id(loan_id)
    if not loan:
        return jsonify({"error": "Loan not found"}), 404
    delete_loan(loan)
    return jsonify({"message": "Loan deleted"}), 200
