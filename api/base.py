from controller.db import (asset_db, budget_db, card_db, 
                           finance_db, income_db, tag_db, 
                           vip_db)

class GetAllDbMix(asset_db.AssetDbMix, budget_db.BudgetDbMix, 
                  card_db.CardDbMix, finance_db.FinanceDbMix, 
                  income_db.IncomeDbMix, tag_db.TagDbMix, 
                  vip_db.VipDbMix):

    def __init__(self):
        super().__init__()

db_mix = GetAllDbMix()
