from enum import Enum
from models.base import Base, HasTenantId, StandardAttr
from models.base import Db as db


class BudgetPeriod(Enum):
    
    DAY = 'day'
    MONTH = 'month'

class Budget(Base, StandardAttr, HasTenantId):
    __tablename__ = 'budget'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    period = db.Column(db.Enum(BudgetPeriod), nullable=False)
    money = db.Column(db.DECIMAL(20, 2), nullable=True)
