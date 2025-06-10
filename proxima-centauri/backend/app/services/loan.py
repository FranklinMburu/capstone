from app.models.loan import Loan
from app.extensions import db

def create_loan(data):
    loan = Loan(**data)
    db.session.add(loan)
    db.session.commit()
    return loan

def get_loan_by_id(loan_id):
    return Loan.query.get(loan_id)

def list_loans():
    return Loan.query.all()

def update_loan(loan, data):
    for key, value in data.items():
        setattr(loan, key, value)
    db.session.commit()
    return loan

def delete_loan(loan):
    db.session.delete(loan)
    db.session.commit()
