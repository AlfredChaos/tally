from common import constant
from models import Base
from models import Db as db

class Property(Base):
    __tablename__ = 'property'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = db.Column(db.String(constant.UUID_FIELD_SIZE), primary_key=True, nullable=False)
    created_at = db.Column(db.Date, nullable=False)
    updated_at = db.Column(db.Date, nullable=False)
    fixed = db.Column(db.DECIMAL(20, 4), nullable=True)
    debt = db.Column(db.DECIMAL(20, 4), nullable=True)
    cash = db.Column(db.DECIMAL(20, 4), nullable=True)
    finance = db.Column(db.DECIMAL(20, 4), nullable=True)