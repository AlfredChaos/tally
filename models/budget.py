from common import constant
from enum import Enum
from models import Base, HasTenantId, StandardAttr
from models import Db as db


class BudgetPeriod(Enum):
    
    DAY = 'day'
    MONTH = 'month'

class Budget(Base, HasTenantId, StandardAttr):
    __tablename__ = 'budget'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    period = db.Column(db.Enum(BudgetPeriod), nullable=False)
    money = db.Column(db.DECIMAL(20, 2), nullable=True)
