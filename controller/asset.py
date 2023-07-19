from controller.db import asset_db

class AssetController(asset_db.AssetDbMix):

    def __init__(self) -> None:
        super().__init__()

    def _get_total(self, asset_db_mix):
        asset_db_mix['total'] = asset_db_mix['fixed'] +\
            asset_db_mix['debt'] + asset_db_mix['cash'] +\
            asset_db_mix['finance']
        return asset_db_mix

    def create_asset(self, params):
        asset_db_mix = super().create_asset(params)
        return  self._get_total(asset_db_mix)

    def update_asset(self, id, params):
        return super().update_asset(id, params)

    def delete_asset(self, id):
        return super().delete_asset(id)
    
    def get_asset(self, id):
        return super().get_asset(id)
    
    def list_assets(self, filters):
        result = []
        assets = super().list_assets(filters)
        for asset in assets:
            result.append(self._get_total(asset))
        return asset

    