from controller.db import tag_db


class TagController(tag_db.TagDbMix):

    def __init__(self) -> None:
        super().__init__()

    def create_tag(self, params):
        return super().create_tag(params)
    
    def update_tag(self, id, params):
        return super().update_tag(id, params)
    
    def delete_tag(self, id):
        return super().delete_tag(id)
    
    def get_tag(self, id):
        return super().get_tag(id)
    
    def list_tags(self, filters):
        return super().list_tags(filters)
    