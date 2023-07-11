from common import constant
from models import Base
from models import Db as db

class Finance(Base):
    __tablename__ = 'finance'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = db.Column(db.String(constant.UUID_FIELD_SIZE), primary_key=True, nullable=False)
    created_at = db.Column(db.Date, nullable=False)
    updated_at = db.Column(db.Date, nullable=False)
    fund = db.Column(db.DECIMAL(20, 4), nullable=True)
    insurance = db.Column(db.DECIMAL(20, 4), nullable=True)
    stock = db.Column(db.DECIMAL(20, 4), nullable=True)
    bank = db.Column(db.DECIMAL(20, 4), nullable=True)