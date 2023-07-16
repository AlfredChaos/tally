from cache import database, log
from common import exception
from controller.db import utils
from models.budget import Budget, BudgetPeriod
from sqlalchemy import and_


LOG = log.get_global_log()
DB = database.get_global_db()


class BudgetDbMix():

    def _make_budget_dict(self, obj):
        return utils.convert_dict(obj)

    def create_budget(self, params):
        user_uuid = params.get('user_uuid', '')
        if not user_uuid:
            err = "user_uuid is required, params = " + str(params)
            LOG.info(err)
            raise exception.InvalidParamsException(err)
        period = params.get('period', BudgetPeriod.DAY)
        money = params.get('money', 0)
        budget = Budget(
            user_uuid=user_uuid,
            period=period,
            money=money
        )
        DB.session.add(budget)
        DB.session.commit()
        return self._make_budget_dict(budget)

    def update_budget(self, id, params):
        try:
            budget = DB.session.query(Budget).filter_by(id=id).first()
            if not budget:
                err = f'updating budget {id} not exist'
                LOG.debug(err)
                raise exception.ObjectUpdateException(err)
            for key, value in params.items():
                setattr(budget, key, value)
            DB.session.commit()
        except Exception as e:
            DB.session.rollback()
            DB.session.flush()
            err = f'updating budget {id} error: {e}'
            LOG.debug(err)
            raise exception.ObjectUpdateException(err)
        return self._make_budget_dict(budget)

    def delete_budget(self, id):
        budget = DB.session.query(Budget).filter_by(id=id).first()
        if not budget:
            err = f'deleting budget {id} not exist'
            LOG.debug(err)
            raise exception.ObjectDeleteException(err)
        try:
            DB.session.delete(budget)
            DB.session.commit()
        except Exception as e:
            DB.session.rollback()
            DB.session.flush()
            err  = f'delete budget {id} error: {e}'
            LOG.error(err)
            raise exception.ObjectDeleteException(err)

    def get_budget(self, id):
        budget = DB.session.query(Budget).filter_by(id=id).first()
        if not budget:
            raise exception.ObjectNotExistException(f'budget {id} not exist')
        return self._make_budget_dict(budget)
    
    def list_budgets(self, filters):
        filter_conditions = []
        for key, value in filters.items():
            filter_conditions.append(getattr(Budget, key) == value)
        try:
            budgets = DB.session.query(Budget).filter(and_(*filter_conditions)).all()
        except Exception as e:
            raise exception.ObjectListException(f'list budgets error: {e}')
        return utils.convert_object_list(budgets)
