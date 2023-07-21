from controller.db import stock_db


class StockController(stock_db.StockDbMix):

    def __init__(self) -> None:
        super().__init__()

    def create_stock(self, params):
        return super().create_stock(params)

    def update_stock(self, id, params):
        return super().update_stock(id, params)

    def delete_stock(self, id):
        return super().delete_stock(id)

    def get_stock(self, id):
        return super().get_stock(id)

    def list_stocks(self, filters):
        return super().list_stocks(filters)
