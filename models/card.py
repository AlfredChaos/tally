from common import constant
from models import Base
from models import Db as db

class Card(Base):
    __tablename__ = 'card'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = db.Column(db.String(constant.UUID_FIELD_SIZE), primary_key=True, nullable=False)
    created_at = db.Column(db.Date, nullable=False)
    updated_at = db.Column(db.Date, nullable=False)
    name = db.Column(db.String(constant.SHORT_TEXT_SIZE), nullable=False)
    bank = db.Column(db.String(constant.SHORT_TEXT_SIZE), nullable=True)
    card_type = db.Column(db.String(constant.SHORT_TEXT_SIZE), nullable=False)
    deposit = db.Column(db.DECIMAL(20, 4), nullable=True)
