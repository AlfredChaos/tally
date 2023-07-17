import apps
from cache import config
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
    init_database_table()
    database_name = config.global_config["Default"]["project"]
    engine_uri = root.db_uri.split(database_name)[0]
    engine = create_engine(engine_uri)
    engine.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
    engine = create_engine(root.db_uri, echo=True)
    base.Base.metadata.create_all(engine)
    print("Create table successfully!")
