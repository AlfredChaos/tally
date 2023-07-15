from datetime import datetime
from sqlalchemy import event
from models.base import Base, HasUserUUID, StandardAttr
from models.base import Db as db

class Asset(Base, StandardAttr, HasUserUUID):
    __tablename__ = 'asset'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    fixed = db.Column(db.DECIMAL(20, 2), nullable=True)
    debt = db.Column(db.DECIMAL(20, 2), nullable=True)
    cash = db.Column(db.DECIMAL(20, 2), nullable=True)
    finance = db.Column(db.DECIMAL(20, 2), nullable=True)


@event.listens_for(Asset, 'before_insert')
@event.listens_for(Asset, 'before_update')
def update_timestamps(mapper, connection, target):
    target.updated_at = datetime.now()
    if not target.created_at:
        target.created_at = datetime.now()
