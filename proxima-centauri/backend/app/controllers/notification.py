from flask import request, jsonify
from app.services.notification import (
    create_notification, get_notification_by_id,
    list_notifications, update_notification, delete_notification
)
from app.schemas.notification import NotificationSchema

notification_schema = NotificationSchema()
notifications_schema = NotificationSchema(many=True)

def create_notification_controller():
    data = request.get_json()
    errors = notification_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    notification = create_notification(data)
    return jsonify(notification_schema.dump(notification)), 201

def get_notification_controller(notification_id):
    notification = get_notification_by_id(notification_id)
    if not notification:
        return jsonify({"error": "Notification not found"}), 404
    return jsonify(notification_schema.dump(notification))

def list_notifications_controller():
    notifications = list_notifications()
    return jsonify(notifications_schema.dump(notifications))

def update_notification_controller(notification_id):
    notification = get_notification_by_id(notification_id)
    if not notification:
        return jsonify({"error": "Notification not found"}), 404
    data = request.get_json()
    notification = update_notification(notification, data)
    return jsonify(notification_schema.dump(notification))

def delete_notification_controller(notification_id):
    notification = get_notification_by_id(notification_id)
    if not notification:
        return jsonify({"error": "Notification not found"}), 404
    delete_notification(notification)
    return jsonify({"message": "Notification deleted"}), 200
