from datetime import datetime
from sqlalchemy import event
from models.base import Base, HasUserUUID, StandardAttr
from models.base import Db as db

class Finance(Base, StandardAttr, HasUserUUID):
    __tablename__ = 'finance'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    fund = db.Column(db.DECIMAL(20, 2), nullable=True)
    insurance = db.Column(db.DECIMAL(20, 2), nullable=True)
    stock = db.Column(db.DECIMAL(20, 2), nullable=True)
    bank = db.Column(db.DECIMAL(20, 2), nullable=True)


@event.listens_for(Finance, 'before_insert')
@event.listens_for(Finance, 'before_update')
def update_timestamps(target):
    target.updated_at = datetime.now()
    if not target.created_at:
        target.created_at = datetime.now()