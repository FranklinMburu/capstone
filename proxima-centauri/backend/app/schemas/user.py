from marshmallow import Schema, fields

class UserCreateSchema(Schema):
    full_name = fields.String(required=True)
    phone_number = fields.String(required=True)
    email = fields.Email(required=False)
    password = fields.String(required=True)

class UserLoginSchema(Schema):
    phone_number = fields.String(required=True)
    password = fields.String(required=True)

class UserResponseSchema(Schema):
    id = fields.String()
    full_name = fields.String()
    phone_number = fields.String()
    email = fields.Email()
    is_verified = fields.Boolean()
    created_at = fields.DateTime()
