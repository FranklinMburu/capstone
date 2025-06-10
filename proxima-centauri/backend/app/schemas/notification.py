from marshmallow import Schema, fields, validate

class NotificationSchema(Schema):
    id = fields.UUID(dump_only=True)
    user_id = fields.UUID(required=True)
    message = fields.String(required=True, validate=validate.Length(min=1))
    type = fields.String(required=True, validate=validate.OneOf(["reminder", "alert", "system"]))
    scheduled_time = fields.DateTime(required=False)
    sent = fields.Boolean()
    created_at = fields.DateTime(dump_only=True)
