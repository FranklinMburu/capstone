from app.models.payment_method import PaymentMethod
from app.extensions import db

def create_payment_method(data):
    pm = PaymentMethod(**data)
    db.session.add(pm)
    db.session.commit()
    return pm

def get_payment_methods_by_user(user_id_bytes):
    return PaymentMethod.query.filter_by(user_id=user_id_bytes).all()

def get_payment_method_by_id(pm_id):
    return PaymentMethod.query.get(pm_id)

def update_payment_method(payment_method, data):
    for key, value in data.items():
        setattr(payment_method, key, value)
    db.session.commit()
    return payment_method