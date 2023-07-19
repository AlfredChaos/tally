from controller.db import budget_db


class BudgetController(budget_db.BudgetDbMix):

    def __init__(self) -> None:
        super().__init__()

    def create_budget(self, params):
        return super().create_budget(params)
    
    def update_budget(self, id, params):
        return super().update_budget(id, params)
    
    def delete_budget(self, id):
        return super().delete_budget(id)
    
    def get_budget(self, id):
        return super().get_budget(id)
    
    def list_budgets(self, filters):
        return super().list_budgets(filters)