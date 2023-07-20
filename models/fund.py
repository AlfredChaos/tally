from common import constant
from datetime import datetime
from sqlalchemy import event
from models.base import Base, HasUserUUID, StandardAttr
from models.base import Db as db

class Fund(Base, StandardAttr, HasUserUUID):
    __tablename__ = 'fund'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    name = db.Column(db.String(constant.SHORT_TEXT_SIZE), nullable=False)
    money = db.Column(db.DECIMAL(20, 2), nullable=True)
    fund_type = db.Column(db.String(constant.SHORT_TEXT_SIZE), nullable=False)
    description = db.Column(db.String(constant.LONG_TEXT_SIZE), nullable=True)
    auto_investment = db.Column(db.Boolean(), nullable=False, default=False)
    auto_investment_strategy = db.Column(db.String(constant.LONG_TEXT_SIZE), nullable=True)
    auto_investment_period = db.Column(db.String(constant.SHORT_TEXT_SIZE), nullable=False)
    auto_investment_money = db.Column(db.DECIMAL(20, 2), nullable=True)
    strategy_type = db.Column(db.String(constant.SHORT_TEXT_SIZE), nullable=False)


@event.listens_for(Fund, 'before_insert')
@event.listens_for(Fund, 'before_update')
def update_timestamps(target):
    target.updated_at = datetime.now()
    if not target.created_at:
        target.created_at = datetime.now()