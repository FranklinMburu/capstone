from flask import request, jsonify
from app.schemas.payment_method import PaymentMethodSchema
from app.services.payment_method import create_payment_method, get_payment_methods_by_user, get_payment_method_by_id
import uuid

payment_method_schema = PaymentMethodSchema()
payment_methods_schema = PaymentMethodSchema(many=True)

def create_payment_method_controller():
    data = request.get_json()
    errors = payment_method_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    pm = create_payment_method(data)
    return payment_method_schema.jsonify(pm), 201

def get_payment_methods_controller(user_id):
    try:
        user_uuid_bytes = uuid.UUID(user_id).bytes
    except ValueError:
        return jsonify({"error": "Invalid user_id format"}), 400

    pms = get_payment_methods_by_user(user_uuid_bytes)
    return payment_methods_schema.jsonify(pms), 200

def get_payment_method_controller(pm_id):
    pm = get_payment_method_by_id(pm_id)
    if not pm:
        return jsonify({"error": "Payment Method not found"}), 404
    return payment_method_schema.jsonify(pm), 200
