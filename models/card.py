from common import constant
from models.base import Base, HasTenantId, StandardAttr
from models.base import Db as db

class Card(Base, HasTenantId, StandardAttr):
    __tablename__ = 'card'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    name = db.Column(db.String(constant.SHORT_TEXT_SIZE), nullable=False)
    bank = db.Column(db.String(constant.SHORT_TEXT_SIZE), nullable=True)
    card_type = db.Column(db.String(constant.SHORT_TEXT_SIZE), nullable=False)
    deposit = db.Column(db.DECIMAL(20, 2), nullable=True)
