from common import constant
from datetime import datetime
from enum import Enum
from sqlalchemy import event
from models.base import Base, HasUserUUID, StandardAttr
from models.base import Db as db


class TagType(Enum):

    ANY = 'any'
    EXPAND = 'expand'
    INCOME = 'income'


class Tag(Base, StandardAttr, HasUserUUID):
    __tablename__ = 'tag'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    name = db.Column(db.String(constant.SHORT_TEXT_SIZE), nullable=False)
    tag_type = db.Column(db.Enum(TagType), nullable=False)


@event.listens_for(Tag, 'before_insert')
@event.listens_for(Tag, 'before_update')
def update_timestamps(mapper, connection, target):
    target.updated_at = datetime.now()
    if not target.created_at:
        target.created_at = datetime.now()