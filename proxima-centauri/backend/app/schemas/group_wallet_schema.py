from marshmallow import Schema, fields

class GroupWalletSchema(Schema):
    id = fields.Str(dump_only=True)
    group_id = fields.Str(required=True)
    balance = fields.Float()
