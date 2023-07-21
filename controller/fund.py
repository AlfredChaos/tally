from controller.db import fund_db

class FundController(fund_db.FundDbMix):

    def __init__(self) -> None:
        super().__init__()

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

    