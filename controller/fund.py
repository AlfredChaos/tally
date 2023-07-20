from controller.db import fund_db

class FundController(fund_db.FundDbMix):

    def __init__(self) -> None:
        super().__init__()

    def _get_total(self, fund_db_mix):
        fund_db_mix['total'] = fund_db_mix['fixed'] +\
            fund_db_mix['debt'] + fund_db_mix['cash'] +\
            fund_db_mix['finance']
        return fund_db_mix

    def create_fund(self, params):
        return super().create_fund(params)

    def update_fund(self, id, params):
        return super().update_fund(id, params)

    def delete_fund(self, id):
        return super().delete_fund(id)
    
    def get_fund(self, id):
        return super().get_fund(id)
    
    def list_funds(self, filters):
        return super().list_funds(filters)

    