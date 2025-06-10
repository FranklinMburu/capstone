import uuid
from marshmallow import Schema, fields, validate, post_load

class LoanSchema(Schema):
    id = fields.Method("get_id", dump_only=True)
    user_id = fields.Method("get_user_id", required=True)
    amount = fields.Decimal(as_string=True, required=True)
    interest_rate = fields.Decimal(as_string=True, required=True)
    term_months = fields.Str(required=True)
    status = fields.Str(dump_only=True)
    is_active = fields.Boolean()
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    def get_id(self, obj):
        return str(uuid.UUID(bytes=obj.id))

    def get_user_id(self, obj):
        return str(uuid.UUID(bytes=obj.user_id))

    @post_load
    def process_user_id(self, data, **kwargs):
        if "user_id" in data and isinstance(data["user_id"], str):
            data["user_id"] = uuid.UUID(data["user_id"]).bytes
        return data
