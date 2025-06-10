from flask import Blueprint, request, jsonify
from app.schemas.group_membership_schema import GroupMembershipSchema
from app.services.group_membership_service import add_member, get_all_memberships, get_membership_by_id, remove_member

group_membership_bp = Blueprint('group_membership_bp', __name__, url_prefix='/group-memberships')
membership_schema = GroupMembershipSchema()
memberships_schema = GroupMembershipSchema(many=True)

@group_membership_bp.route('', methods=['POST'])
def create():
    data = request.get_json()
    errors = membership_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    membership = add_member(data)
    return membership_schema.jsonify(membership), 201

@group_membership_bp.route('', methods=['GET'])
def get_all():
    memberships = get_all_memberships()
    return memberships_schema.jsonify(memberships), 200

@group_membership_bp.route('/<int:membership_id>', methods=['GET'])
def get_one(membership_id):
    membership = get_membership_by_id(membership_id)
    if not membership:
        return jsonify({"message": "Membership not found"}), 404
    return membership_schema.jsonify(membership), 200

@group_membership_bp.route('/<int:membership_id>', methods=['DELETE'])
def delete(membership_id):
    membership = get_membership_by_id(membership_id)
    if not membership:
        return jsonify({"message": "Membership not found"}), 404
    remove_member(membership)
    return jsonify({"message": "Membership removed"}), 200
