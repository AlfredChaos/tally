from controller.db import vip_db


class VipController(vip_db.VipDbMix):

    def __init__(self) -> None:
        super().__init__()

    def create_vip(self, params):
        return super().create_vip(params)
    
    def update_vip(self, id, params):
        return super().update_vip(id, params)
    
    def delete_vip(self, id):
        return super().delete_vip(id)
    
    def get_vip(self, id):
        return super().get_vip(id)
    
    def list_vips(self, filters):
        return super().list_vips(filters)