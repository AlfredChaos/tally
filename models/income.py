from common import constant
from datetime import datetime
from sqlalchemy import event
from models.base import Base, HasUserUUID, StandardAttr
from models.base import Db as db


class Income(Base, StandardAttr, HasUserUUID):
    __tablename__ = 'income'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    name = db.Column(db.String(constant.SHORT_TEXT_SIZE), nullable=False)
    description = db.Column(db.String(constant.LONG_TEXT_SIZE), nullable=True)
    tag_id = db.Column(db.String(constant.UUID_FIELD_SIZE), db.ForeignKey('tag.id'))
    income = db.Column(db.DECIMAL(20, 2), nullable=True, default=0)
    tag = db.relationship('Tag', backref='income')


@event.listens_for(Income, 'before_insert')
@event.listens_for(Income, 'before_update')
def update_timestamps(mapper, connection, target):
    target.updated_at = datetime.now()
    if not target.created_at:
        target.created_at = datetime.now()