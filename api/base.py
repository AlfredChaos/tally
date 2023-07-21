from controller import (asset, budget, card, income, tag, vip, fund, finance, insurance)

class GetAllDbMix(asset.AssetController, budget.BudgetController, 
                  card.CardController, finance.FinanceController, 
                  income.IncomeController, tag.TagController, 
                  vip.VipController, fund.FundController,
                  insurance.InsuranceController):

    def __init__(self):
        super().__init__()

db_mix = GetAllDbMix()
