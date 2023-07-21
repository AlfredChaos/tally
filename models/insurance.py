from common import constant
from datetime import datetime
from sqlalchemy import event
from models.base import Base, HasUserUUID, StandardAttr
from models.base import Db as db

class Insurance(Base, StandardAttr, HasUserUUID):
    __tablename__ = 'insurance'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    name = db.Column(db.String(constant.SHORT_TEXT_SIZE), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.String(constant.LONG_TEXT_SIZE), nullable=True)
    insurance_type = db.Column(db.String(constant.SHORT_TEXT_SIZE), nullable=False)
    insurance_period = db.Column(db.String(constant.SHORT_TEXT_SIZE), nullable=False)
    money_per_period = db.Column(db.DECIMAL(20, 2), nullable=True)
    amount = db.Column(db.DECIMAL(20, 2), nullable=True)
    excepted_income = db.Column(db.DECIMAL(20, 2), nullable=True)


@event.listens_for(Insurance, 'before_insert')
@event.listens_for(Insurance, 'before_update')
def update_timestamps(target):
    target.updated_at = datetime.now()
    if not target.created_at:
        target.created_at = datetime.now()