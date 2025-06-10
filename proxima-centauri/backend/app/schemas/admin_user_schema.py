from marshmallow import Schema, fields, validate

class AdminUserSchema(Schema):
    id = fields.UUID(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(min=1))
    email = fields.Email(required=True)
    password = fields.String(required=True, load_only=True)
    is_superadmin = fields.Boolean()
    is_active = fields.Boolean()
    created_at = fields.DateTime(dump_only=True)
