from controller.db import income_db


class IncomeController(income_db.IncomeDbMix):

    def __init__(self) -> None:
        super().__init__()

    def create_income(self, params):
        return super().create_income(params)
    
    def update_income(self, id, params):
        return super().update_income(id, params)
    
    def delete_income(self, id):
        return super().delete_income(id)
    
    def get_income(self, id):
        return super().get_income(id)
    
    def list_incomes(self, filters):
        return super().list_incomes(filters)
