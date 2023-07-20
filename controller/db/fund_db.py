from cache import database, log
from common import exception
from controller.db import utils
from models.fund import Fund
from sqlalchemy import and_


LOG = log.get_global_log()
DB = database.get_global_db()


class FundDbMix():

    def _make_fund_dict(self, obj):
        return utils.convert_dict(obj)

    def create_fund(self, params):
        user_uuid = params.get('user_uuid', '')
        if not user_uuid:
            err = "user_uuid is required, params = " + str(params)
            LOG.info(err)
            raise exception.InvalidParamsException(err)
        name = params.get('name', '')
        tag_id = params.get('tag_id', '')
        fund_num = params.get('fund', 0)
        description = params.get('description', '')
        fund = Fund(
            user_uuid=user_uuid,
            name=name,
            tag_id=tag_id,
            fund=fund_num,
            description=description
        )
        DB.session.add(fund)
        DB.session.commit()
        return self._make_fund_dict(fund)
 
    def update_fund(self, id, params):
        try:
            fund = DB.session.query(Fund).filter_by(id=id).first()
            if not fund:
                err = f'updating fund {id} not exist'
                LOG.debug(err)
                raise exception.ObjectUpdateException(err)
            for key, value in params.items():
                setattr(fund, key, value)
            DB.session.commit()
        except Exception as e:
            DB.session.rollback()
            DB.session.flush()
            err = f'updating fund {id} error: {e}'
            LOG.debug(err)
            raise exception.ObjectUpdateException(err)
        return self._make_fund_dict(fund)

    def delete_fund(self, id):
        fund = DB.session.query(Fund).filter_by(id=id).first()
        if not fund:
            err = f'deleting fund {id} not exist'
            LOG.debug(err)
            raise exception.ObjectDeleteException(err)
        try:
            DB.session.delete(fund)
            DB.session.commit()
        except Exception as e:
            DB.session.rollback()
            DB.session.flush()
            err  = f'delete fund {id} error: {e}'
            LOG.error(err)
            raise exception.ObjectDeleteException(err)

    def get_fund(self, id):
        fund = DB.session.query(Fund).filter_by(id=id).first()
        if not fund:
            raise exception.ObjectNotExistException(f'fund {id} not exist')
        return self._make_fund_dict(fund)
    
    def list_funds(self, filters):
        filter_conditions = []
        for key, value in filters.items():
            filter_conditions.append(getattr(Fund, key) == value)
        try:
            funds = DB.session.query(Fund).filter(and_(*filter_conditions)).all()
        except Exception as e:
            raise exception.ObjectListException(f'list funds error: {e}')
        return utils.convert_object_list(funds)
