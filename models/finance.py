from models.base import Base, HasTenantId, StandardAttr
from models.base import Db as db

class Finance(Base, StandardAttr, HasTenantId):
    __tablename__ = 'finance'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    fund = db.Column(db.DECIMAL(20, 2), nullable=True)
    insurance = db.Column(db.DECIMAL(20, 2), nullable=True)
    stock = db.Column(db.DECIMAL(20, 2), nullable=True)
    bank = db.Column(db.DECIMAL(20, 2), nullable=True)