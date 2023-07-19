from controller import (asset, budget, card, income, tag, vip)
from controller.db import (budget_db, card_db, 
                           finance_db, income_db, tag_db, 
                           vip_db)

class GetAllDbMix(asset.AssetController, budget.BudgetController, 
                  card.CardController, finance_db.FinanceDbMix, 
                  income.IncomeController, tag.TagController, 
                  vip.VipController):

    def __init__(self):
        super().__init__()

db_mix = GetAllDbMix()
