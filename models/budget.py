from datetime import datetime
from sqlalchemy import event
from enum import Enum
from models.base import Base, HasUserUUID, StandardAttr
from models.base import Db as db


class BudgetPeriod(Enum):
    
    DAY = 'day'
    MONTH = 'month'

class Budget(Base, StandardAttr, HasUserUUID):
    __tablename__ = 'budget'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    period = db.Column(db.Enum(BudgetPeriod), nullable=False)
    money = db.Column(db.DECIMAL(20, 2), nullable=True)


@event.listens_for(Budget, 'before_insert')
@event.listens_for(Budget, 'before_update')
def update_timestamps(target):
    target.updated_at = datetime.now()
    if not target.created_at:
        target.created_at = datetime.now()