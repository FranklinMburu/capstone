from app.extensions import db
from app.models.group_setting import GroupSetting

def create_group_setting(data):
    setting = GroupSetting(**data)
    db.session.add(setting)
    db.session.commit()
    return setting

def get_all_group_settings():
    return GroupSetting.query.all()

def get_group_setting_by_id(setting_id):
    return GroupSetting.query.get(setting_id)

def update_group_setting(setting, data):
    for key, value in data.items():
        setattr(setting, key, value)
    db.session.commit()
    return setting

def delete_group_setting(setting):
    db.session.delete(setting)
    db.session.commit()
