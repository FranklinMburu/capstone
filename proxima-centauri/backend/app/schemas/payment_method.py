import uuid
from marshmallow import Schema, fields, validate, post_load

class PaymentMethodSchema(Schema):
    id = fields.Method("get_id", dump_only=True)
    user_id = fields.Method("get_user_id", required=True)
    type = fields.Str(required=True, validate=validate.OneOf(["card", "bank_account", "mobile_money"]))
    provider = fields.Str(required=True)
    account_number = fields.Str(required=True)
    expiry_date = fields.Str(allow_none=True)
    created_at = fields.DateTime(dump_only=True)

    def get_id(self, obj):
        return str(uuid.UUID(bytes=obj.id))

    def get_user_id(self, obj):
        return str(uuid.UUID(bytes=obj.user_id))

    @post_load
    def process_user_id(self, data, **kwargs):
        if "user_id" in data and isinstance(data["user_id"], str):
            data["user_id"] = uuid.UUID(data["user_id"]).bytes
        return data
