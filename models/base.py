from cache import database
from common import constant
from sqlalchemy.ext.declarative import declarative_base
from oslo_utils import uuidutils

Base = declarative_base()
Db = database.get_global_db()


class StandardAttr(object):

    id = Db.Column(Db.String(constant.UUID_FIELD_SIZE), primary_key=True, default=uuidutils.generate_uuid)
    created_at = Db.Column(Db.Date, nullable=False)
    updated_at = Db.Column(Db.Date, nullable=False)


class HasUserUUID(object):

    user_uuid = Db.Column(Db.String(constant.UUID_FIELD_SIZE), index=True, nullable=False)
