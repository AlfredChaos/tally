from controller.db import card_db


class CardController(card_db.CardDbMix):

    def __init__(self) -> None:
        super().__init__()

    def create_card(self, params):
        return super().create_card(params)
    
    def update_card(self, id, params):
        return super().update_card(id, params)
    
    def delete_card(self, id):
        return super().delete_card(id)
    
    def get_card(self, id):
        return super().get_card(id)
    
    def list_cards(self, filters):
        return super().list_cards(filters)