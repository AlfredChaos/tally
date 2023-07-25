from apps import root
from cache import config
from models import (base, budget, card, fund, income, asset, tag, vip, stock, insurance)
from sqlalchemy import create_engine


def init_database_table():
    budget.Budget()
    card.Card()
    fund.Fund()
    income.Income()
    asset.Asset()
    tag.Tag()
    vip.Vip()
    stock.Stock()
    insurance.Insurance()


if __name__ == '__main__':
    init_database_table()
    database_name = config.global_config["Default"]["project"]
    engine_uri = root.db_uri.split(database_name)[0]
    engine = create_engine(engine_uri)
    engine.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
    engine = create_engine(root.db_uri, echo=True)
    base.Base.metadata.create_all(engine)
    print("Create table successfully!")
