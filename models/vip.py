from common import constant
from models.base import Base, HasUserUUID, StandardAttr
from models.base import Db as db

class Vip(Base, StandardAttr, HasUserUUID):
    __tablename__ = 'vip'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    name = db.Column(db.String(constant.SHORT_TEXT_SIZE), nullable=False)
    fee = db.Column(db.DECIMAL(20, 2), nullable=False)
    deduct_date = db.Column(db.String(constant.SHORT_TEXT_SIZE), nullable=False)
    deduct_period = db.Column(db.String(constant.SHORT_TEXT_SIZE), nullable=False)
    payment_channel = db.Column(db.String(constant.SHORT_TEXT_SIZE), nullable=False)
