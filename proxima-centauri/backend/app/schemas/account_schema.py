from marshmallow import Schema, fields, validate

class AccountSchema(Schema):
    id = fields.UUID(dump_only=True)
    user_id = fields.UUID(required=True)
    account_name = fields.String(required=True, validate=validate.Length(min=1))
    account_type = fields.String(required=True, validate=validate.OneOf(["savings", "current", "wallet"]))
    balance = fields.Decimal(as_string=True)
    currency = fields.String(required=False)
    is_active = fields.Boolean()
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
