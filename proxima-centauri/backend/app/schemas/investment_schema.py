from marshmallow import Schema, fields, validate

class InvestmentSchema(Schema):
    id = fields.UUID(dump_only=True)
    user_id = fields.UUID(required=True)
    type = fields.String(required=True, validate=validate.OneOf(["stocks", "bonds", "fund"]))
    amount = fields.Decimal(required=True, as_string=True)
    returns = fields.Decimal(as_string=True)
    description = fields.String()
    created_at = fields.DateTime(dump_only=True)
