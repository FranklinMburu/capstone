from marshmallow import Schema, fields

class GroupSettingSchema(Schema):
    id = fields.Str(dump_only=True)
    group_id = fields.Str(required=True)
    min_signatories = fields.Int()
    rules = fields.Str()
