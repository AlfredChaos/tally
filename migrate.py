import apps
from cache import database
from models import (base, budget, card, finance, income, asset, tag, vip)
from sqlalchemy import create_engine


def init_database_table():
    budget.Budget()
    card.Card()
    finance.Finance()
    income.Income()
    asset.Asset()
    tag.Tag()
    vip.Vip()
    

if __name__ == '__main__':
    root = apps.RegisterApp()
    database.global_db = root.db
    init_database_table()
    engine = create_engine(root.db_uri, echo=True)
    base.Base.metadata.create_all(engine)
    print("Create table successfully!")