from marshmallow import Schema, fields, validate

class TransactionSchema(Schema):
    id = fields.UUID(dump_only=True)
    user_id = fields.UUID(required=True)
    account_id = fields.UUID(required=True)
    type = fields.String(required=True, validate=validate.OneOf(["deposit", "withdrawal", "service_charge"]))
    amount = fields.Decimal(required=True, as_string=True)
    method = fields.String(required=True, validate=validate.OneOf(["mpesa", "bank", "manual"]))
    mpesa_ref = fields.String(allow_none=True)
    status = fields.String(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
