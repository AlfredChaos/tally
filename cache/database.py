import sqlalchemy as db


global_db = None

def get_global_db():
    global global_db
    if not global_db:
        global_db = db
    return global_db