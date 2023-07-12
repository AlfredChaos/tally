from common import constant
from models import Base, HasTenantId, StandardAttr
from models import Db as db

class Income(Base, HasTenantId, StandardAttr):
    __tablename__ = 'income'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    name = db.Column(db.String(constant.SHORT_TEXT_SIZE), nullable=False)
    tag_id = db.Column(db.String(constant.UUID_FIELD_SIZE), db.ForeignKey('tag.id'))
    income = db.Column(db.DECIMAL(20, 2), nullable=True, default=0)
    tag = db.relationship('Tag', backref='income')