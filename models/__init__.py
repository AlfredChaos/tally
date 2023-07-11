from cache import database, log
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
Db = database.get_global_db()
Log = log.get_global_log()
