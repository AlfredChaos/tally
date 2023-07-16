from cache import database, log
from common import exception
from controller.db import utils
from models.finance import Finance
from sqlalchemy import and_


LOG = log.get_global_log()
DB = database.get_global_db()


class FinanceDbMix():

    def _make_finance_dict(self, obj):
        return utils.convert_dict(obj)

    def create_finance(self, params):
        user_uuid = params.get('user_uuid', '')
        if not user_uuid:
            err = "user_uuid is required, params = " + str(params)
            LOG.info(err)
            raise exception.InvalidParamsException(err)
        fund = params.get('fund', 0)
        insurance = params.get('insurance', 0)
        stock = params.get('stock', 0)
        bank = params.get('bank', 0)
        finance = Finance(
            user_uuid=user_uuid,
            fund=fund,
            insurance=insurance,
            stock=stock,
            bank=bank,
        )
        DB.session.add(finance)
        DB.session.commit()
        return self._make_finance_dict(finance)

    def update_finance(self, id, params):
        try:
            finance = DB.session.query(Finance).filter_by(id=id).first()
            if not finance:
                err = f'updating finance {id} not exist'
                LOG.debug(err)
                raise exception.ObjectUpdateException(err)
            for key, value in params.items():
                setattr(finance, key, value)
            DB.session.commit()
        except Exception as e:
            DB.session.rollback()
            DB.session.flush()
            err = f'updating finance {id} error: {e}'
            LOG.debug(err)
            raise exception.ObjectUpdateException(err)
        return self._make_finance_dict(finance)

    def delete_finance(self, id):
        finance = DB.session.query(Finance).filter_by(id=id).first()
        if not finance:
            err = f'deleting finance {id} not exist'
            LOG.debug(err)
            raise exception.ObjectDeleteException(err)
        try:
            DB.session.delete(finance)
            DB.session.commit()
        except Exception as e:
            DB.session.rollback()
            DB.session.flush()
            err  = f'delete finance {id} error: {e}'
            LOG.error(err)
            raise exception.ObjectDeleteException(err)

    def get_finance(self, id):
        finance = DB.session.query(Finance).filter_by(id=id).first()
        if not finance:
            raise exception.ObjectNotExistException(f'finance {id} not exist')
        return self._make_finance_dict(finance)
    
    def list_finances(self, filters):
        filter_conditions = []
        for key, value in filters.items():
            filter_conditions.append(getattr(Finance, key) == value)
        try:
            finances = DB.session.query(Finance).filter(and_(*filter_conditions)).all()
        except Exception as e:
            raise exception.ObjectListException(f'list finances error: {e}')
        return utils.convert_object_list(finances)
