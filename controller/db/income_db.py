from cache import database, log
from common import exception
from controller.db import utils
from models.income import Income
from sqlalchemy import and_


LOG = log.get_global_log()
DB = database.get_global_db()


class IncomeDbMix():

    def _make_income_dict(self, obj):
        return utils.convert_dict(obj)

    def create_income(self, params):
        user_uuid = params.get('user_uuid', '')
        if not user_uuid:
            err = "user_uuid is required, params = " + str(params)
            LOG.info(err)
            raise exception.InvalidParamsException(err)
        name = params.get('name', '')
        tag_id = params.get('tag_id', '')
        income_num = params.get('income', 0)
        description = params.get('description', '')
        income = Income(
            user_uuid=user_uuid,
            name=name,
            tag_id=tag_id,
            income=income_num,
            description=description
        )
        DB.session.add(income)
        DB.session.commit()
        return self._make_income_dict(income)
 
    def update_income(self, id, params):
        try:
            income = DB.session.query(Income).filter_by(id=id).first()
            if not income:
                err = f'updating income {id} not exist'
                LOG.debug(err)
                raise exception.ObjectUpdateException(err)
            for key, value in params.items():
                setattr(income, key, value)
            DB.session.commit()
        except Exception as e:
            DB.session.rollback()
            DB.session.flush()
            err = f'updating income {id} error: {e}'
            LOG.debug(err)
            raise exception.ObjectUpdateException(err)
        return self._make_income_dict(income)

    def delete_income(self, id):
        income = DB.session.query(Income).filter_by(id=id).first()
        if not income:
            err = f'deleting income {id} not exist'
            LOG.debug(err)
            raise exception.ObjectDeleteException(err)
        try:
            DB.session.delete(income)
            DB.session.commit()
        except Exception as e:
            DB.session.rollback()
            DB.session.flush()
            err  = f'delete income {id} error: {e}'
            LOG.error(err)
            raise exception.ObjectDeleteException(err)

    def get_income(self, id):
        income = DB.session.query(Income).filter_by(id=id).first()
        if not income:
            raise exception.ObjectNotExistException(f'income {id} not exist')
        return self._make_income_dict(income)
    
    def list_incomes(self, filters):
        filter_conditions = []
        for key, value in filters.items():
            filter_conditions.append(getattr(Income, key) == value)
        try:
            incomes = DB.session.query(Income).filter(and_(*filter_conditions)).all()
        except Exception as e:
            raise exception.ObjectListException(f'list incomes error: {e}')
        return utils.convert_object_list(incomes)
