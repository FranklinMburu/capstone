from marshmallow import Schema, fields

class WalletSchema(Schema):
    id = fields.UUID(dump_only=True)
    user_id = fields.UUID(required=True)
    balance = fields.Decimal(as_string=True, dump_only=True)
    last_updated = fields.DateTime(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
