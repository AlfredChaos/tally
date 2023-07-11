from common import constant
from models import Base
from models import Db as db

class Tag(Base):
    __tablename__ = 'tag'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = db.Column(db.String(constant.UUID_FIELD_SIZE), primary_key=True, nullable=False)
    created_at = db.Column(db.Date, nullable=False)
    updated_at = db.Column(db.Date, nullable=False)
    name = db.Column(db.String(constant.SHORT_TEXT_SIZE), nullable=False)
