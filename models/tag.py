from common import constant
from models.base import Base, HasTenantId, StandardAttr
from models.base import Db as db

class Tag(Base, HasTenantId, StandardAttr):
    __tablename__ = 'tag'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    name = db.Column(db.String(constant.SHORT_TEXT_SIZE), nullable=False)
