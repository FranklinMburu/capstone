from app.models.notification import Notification
from app.extensions import db

def create_notification(data):
    notification = Notification(**data)
    db.session.add(notification)
    db.session.commit()
    return notification

def get_notification_by_id(notification_id):
    return Notification.query.get(notification_id)

def list_notifications():
    return Notification.query.all()

def update_notification(notification, data):
    for key, value in data.items():
        setattr(notification, key, value)
    db.session.commit()
    return notification

def delete_notification(notification):
    db.session.delete(notification)
    db.session.commit()
