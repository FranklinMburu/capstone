from flask import Blueprint, request, jsonify
from app.schemas.group_schema import GroupSchema
from app.services.group_service import create_group, get_all_groups, get_group_by_id, update_group, delete_group

group_bp = Blueprint('group_bp', __name__, url_prefix='/groups')
group_schema = GroupSchema()
groups_schema = GroupSchema(many=True)

@group_bp.route('', methods=['POST'])
def create():
    data = request.get_json()
    errors = group_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    group = create_group(data)
    return group_schema.jsonify(group), 201

@group_bp.route('', methods=['GET'])
def get_all():
    groups = get_all_groups()
    return groups_schema.jsonify(groups), 200

@group_bp.route('/<int:group_id>', methods=['GET'])
def get_one(group_id):
    group = get_group_by_id(group_id)
    if not group:
        return jsonify({"message": "Group not found"}), 404
    return group_schema.jsonify(group), 200

@group_bp.route('/<int:group_id>', methods=['PUT'])
def update(group_id):
    group = get_group_by_id(group_id)
    if not group:
        return jsonify({"message": "Group not found"}), 404
    data = request.get_json()
    errors = group_schema.validate(data, partial=True)
    if errors:
        return jsonify(errors), 400
    updated_group = update_group(group, data)
    return group_schema.jsonify(updated_group), 200

@group_bp.route('/<int:group_id>', methods=['DELETE'])
def delete(group_id):
    group = get_group_by_id(group_id)
    if not group:
        return jsonify({"message": "Group not found"}), 404
    delete_group(group)
    return jsonify({"message": "Group deleted"}), 200
