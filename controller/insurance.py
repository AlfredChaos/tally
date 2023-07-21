from controller.db import insurance_db


class InsuranceController(insurance_db.InsuranceDbMix):

    def __init__(self) -> None:
        super().__init__()

    def create_insurance(self, params):
        return super().create_insurance(params)
    
    def update_insurance(self, id, params):
        return super().update_insurance(id, params)
    
    def delete_insurance(self, id):
        return super().delete_insurance(id)
    
    def get_insurance(self, id):
        return super().get_insurance(id)
    
    def list_insurances(self, filters):
        return super().list_insurances(filters)
