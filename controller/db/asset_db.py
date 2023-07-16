from cache import database, log
from common import exception
from controller.db import utils
from models.asset import Asset
from sqlalchemy import and_


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
        return self._make_asset_dict(asset)

    def update_asset(self, id, params):
        try:
            asset = DB.session.query(Asset).filter_by(id=id).first()
            if not asset:
                err = f'updating asset {id} not exist'
                LOG.debug(err)
                raise exception.ObjectUpdateException(err)
            for key, value in params.items():
                setattr(asset, key, value)
            DB.session.commit()
        except Exception as e:
            DB.session.rollback()
            DB.session.flush()
            err = f'updating asset {id} error: {e}'
            LOG.debug(err)
            raise exception.ObjectUpdateException(err)
        return self._make_asset_dict(asset)

    def delete_asset(self, id):
        asset = DB.session.query(Asset).filter_by(id=id).first()
        if not asset:
            err = f'deleting asset {id} not exist'
            LOG.debug(err)
            raise exception.ObjectDeleteException(err)
        try:
            DB.session.delete(asset)
            DB.session.commit()
        except Exception as e:
            DB.session.rollback()
            DB.session.flush()
            err  = f'delete asset {id} error: {e}'
            LOG.error(err)
            raise exception.ObjectDeleteException(err)

    def get_asset(self, id):
        asset = DB.session.query(Asset).filter_by(id=id).first()
        if not asset:
            raise exception.ObjectNotExistException(f'asset {id} not exist')
        return self._make_asset_dict(asset)
    
    def list_assets(self, filters):
        filter_conditions = []
        for key, value in filters.items():
            filter_conditions.append(getattr(Asset, key) == value)
        try:
            assets = DB.session.query(Asset).filter(and_(*filter_conditions)).all()
        except Exception as e:
            raise exception.ObjectListException(f'list assets error: {e}')
        return utils.convert_object_list(assets)
