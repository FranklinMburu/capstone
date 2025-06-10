from marshmallow import Schema, fields, validate

class PermissionSchema(Schema):
    id = fields.UUID(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(min=2))
    description = fields.String()
    created_at = fields.DateTime(dump_only=True)
