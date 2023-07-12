from models import Base, HasTenantId, StandardAttr
from models import Db as db

class Finance(Base, HasTenantId, StandardAttr):
    __tablename__ = 'finance'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    fund = db.Column(db.DECIMAL(20, 2), nullable=True)
    insurance = db.Column(db.DECIMAL(20, 2), nullable=True)
    stock = db.Column(db.DECIMAL(20, 2), nullable=True)
    bank = db.Column(db.DECIMAL(20, 2), nullable=True)