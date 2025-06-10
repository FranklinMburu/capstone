from flask import Blueprint, request, jsonify
from app.schemas.group_setting_schema import GroupSettingSchema
from app.services.group_setting_service import create_group_setting, get_all_group_settings, get_group_setting_by_id, update_group_setting, delete_group_setting

group_setting_bp = Blueprint('group_setting_bp', __name__, url_prefix='/group-settings')
setting_schema = GroupSettingSchema()
settings_schema = GroupSettingSchema(many=True)

@group_setting_bp.route('', methods=['POST'])
def create():
    data = request.get_json()
    errors = setting_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    setting = create_group_setting(data)
    return setting_schema.jsonify(setting), 201

@group_setting_bp.route('', methods=['GET'])
def get_all():
    settings = get_all_group_settings()
    return settings_schema.jsonify(settings), 200

@group_setting_bp.route('/<int:setting_id>', methods=['GET'])
def get_one(setting_id):
    setting = get_group_setting_by_id(setting_id)
    if not setting:
        return jsonify({"message": "Setting not found"}), 404
    return setting_schema.jsonify(setting), 200

@group_setting_bp.route('/<int:setting_id>', methods=['PUT'])
def update(setting_id):
    setting = get_group_setting_by_id(setting_id)
    if not setting:
        return jsonify({"message": "Setting not found"}), 404
    data = request.get_json()
    errors = setting_schema.validate(data, partial=True)
    if errors:
        return jsonify(errors), 400
    updated_setting = update_group_setting(setting, data)
    return setting_schema.jsonify(updated_setting), 200

@group_setting_bp.route('/<int:setting_id>', methods=['DELETE'])
def delete(setting_id):
    setting = get_group_setting_by_id(setting_id)
    if not setting:
        return jsonify({"message": "Setting not found"}), 404
    delete_group_setting(setting)
    return jsonify({"message": "Setting deleted"}), 200
