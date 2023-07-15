from cache import database, log
from common import exception
from controller.db import utils
from models.asset import Asset

LOG = log.get_global_log()
DB = database.get_global_db()

class AssetDbMix():
    
    def _make_asset_dict(self, obj):
        return utils.convert_dict(obj)
    
    def create_asset(self, params):
        user_uuid = params.get('user_uuid', '')
        if not user_uuid:
            err = "user_uuid is required, params = " + str(params)
            LOG.info(err)
            raise exception.InvalidParamsException(err)
        fixed = params.get('fixed', 0)
        debt = params.get('debt', 0)
        cash = params.get('cash', 0)
        finance = params.get('finance', 0)
        asset = Asset(
            user_uuid=user_uuid,
            fixed=fixed,
            debt=debt,
            cash=cash,
            finance=finance
        )
        DB.session.add(asset)
        DB.session.commit()

    def update():
        pass

    def delete():
        pass

    def get():
        pass            