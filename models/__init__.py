from cache import database, log
from common import constant
from sqlalchemy.ext.declarative import declarative_base
from oslo_utils import uuidutils

Base = declarative_base()
Db = database.get_global_db()
Log = log.get_global_log()


class HasTenantId(object):

    tenant_id = Db.Column(Db.String(constant.UUID_FIELD_SIZE), index=True)


class StandardAttr(object):

    id = Db.Column(Db.String(constant.UUID_FIELD_SIZE), primary_key=True, default=uuidutils.generate_uuid)
    created_at = Db.Column(Db.Date, nullable=False)
    updated_at = Db.Column(Db.Date, nullable=False)