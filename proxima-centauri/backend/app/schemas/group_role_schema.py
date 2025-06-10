from marshmallow import Schema, fields

class GroupRoleSchema(Schema):
    id = fields.Str(dump_only=True)
    group_id = fields.Str(required=True)
    name = fields.Str(required=True)
    description = fields.Str()
