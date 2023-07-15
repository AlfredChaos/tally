from controller.db import asset_db

class GetAllDbMix(asset_db.AssetDbMix):

    def __init__(self):
        super().__init__()

db_mix = GetAllDbMix()
