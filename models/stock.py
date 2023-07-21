from common import constant
from datetime import datetime
from sqlalchemy import event
from models.base import Base, HasUserUUID, StandardAttr
from models.base import Db as db

class Stock(Base, StandardAttr, HasUserUUID):
    __tablename__ = 'stock'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    name = db.Column(db.String(constant.SHORT_TEXT_SIZE), nullable=False)
    money = db.Column(db.DECIMAL(20, 2), nullable=True)
    description = db.Column(db.String(constant.LONG_TEXT_SIZE), nullable=True)


@event.listens_for(Stock, 'before_insert')
@event.listens_for(Stock, 'before_update')
def update_timestamps(target):
    target.updated_at = datetime.now()
    if not target.created_at:
        target.created_at = datetime.now()