from app.models.investment import Investment
from app.extensions import db

def create_investment(data):
    investment = Investment(**data)
    db.session.add(investment)
    db.session.commit()
    return investment

def get_investment_by_id(investment_id):
    return Investment.query.get(investment_id)

def list_investments():
    return Investment.query.all()

def update_investment(investment, data):
    for key, value in data.items():
        setattr(investment, key, value)
    db.session.commit()
    return investment

def delete_investment(investment):
    db.session.delete(investment)
    db.session.commit()
