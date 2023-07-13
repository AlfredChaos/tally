from models.base import Base, HasTenantId, StandardAttr
from models.base import Db as db

class Asset(Base, StandardAttr, HasTenantId):
    __tablename__ = 'asset'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    fixed = db.Column(db.DECIMAL(20, 2), nullable=True)
    debt = db.Column(db.DECIMAL(20, 2), nullable=True)
    cash = db.Column(db.DECIMAL(20, 2), nullable=True)
    finance = db.Column(db.DECIMAL(20, 2), nullable=True)