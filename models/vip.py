from common import constant
from models import Base
from models import Db as db

class Vip(Base):
    __tablename__ = 'vip'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = db.Column(db.String(constant.UUID_FIELD_SIZE), primary_key=True, nullable=False)
    created_at = db.Column(db.Date, nullable=False)
    updated_at = db.Column(db.Date, nullable=False)
    name = db.Column(db.String(constant.SHORT_TEXT_SIZE), nullable=False)
    fee = db.Column(db.DECIMAL(20, 4), nullable=False)
    deduct_date = db.Column(db.String(constant.SHORT_TEXT_SIZE), nullable=False)
    deduct_period = db.Column(db.String(constant.SHORT_TEXT_SIZE), nullable=False)
    payment_channel = db.Column(db.String(constant.SHORT_TEXT_SIZE), nullable=False)
