import uuid
from flask import request, jsonify
from app.extensions import db
from app.models.group_setting import GroupSetting
from app.schemas.group_setting_schema import GroupSettingSchema

group_setting_schema = GroupSettingSchema()
group_settings_schema = GroupSettingSchema(many=True)

def create_group_setting():
    data = request.get_json()
    errors = group_setting_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    setting = GroupSetting(
        id=str(uuid.uuid4()),
        group_id=data['group_id'],
        min_signatories=data.get('min_signatories', 1),
        rules=data.get('rules')
    )
    db.session.add(setting)
    db.session.commit()
    return group_setting_schema.jsonify(setting), 201

def get_group_settings():
    settings = GroupSetting.query.all()
    return group_settings_schema.jsonify(settings), 200

def get_group_setting(setting_id):
    setting = GroupSetting.query.get(setting_id)
    if not setting:
        return jsonify({'message': 'Setting not found'}), 404
    return group_setting_schema.jsonify(setting), 200

def update_group_setting(setting_id):
    setting = GroupSetting.query.get(setting_id)
    if not setting:
        return jsonify({'message': 'Setting not found'}), 404

    data = request.get_json()
    errors = group_setting_schema.validate(data, partial=True)
    if errors:
        return jsonify(errors), 400

    if 'min_signatories' in data:
        setting.min_signatories = data['min_signatories']
    if 'rules' in data:
        setting.rules = data['rules']

    db.session.commit()
    return group_setting_schema.jsonify(setting), 200

def delete_group_setting(setting_id):
    setting = GroupSetting.query.get(setting_id)
    if not setting:
        return jsonify({'message': 'Setting not found'}), 404

    db.session.delete(setting)
    db.session.commit()
    return jsonify({'message': 'Setting deleted'}), 200
