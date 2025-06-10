from marshmallow import Schema, fields

class GroupMembershipSchema(Schema):
    id = fields.Str(dump_only=True)
    user_id = fields.Str(required=True)
    group_id = fields.Str(required=True)
    joined_at = fields.DateTime(dump_only=True)
