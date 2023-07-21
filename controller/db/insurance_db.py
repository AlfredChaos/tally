from cache import database, log
from common import exception
from controller.db import utils
from models.insurance import Insurance
from sqlalchemy import and_


LOG = log.get_global_log()
DB = database.get_global_db()


class InsuranceDbMix():

    def _make_insurance_dict(self, obj):
        return utils.convert_dict(obj)

    def create_insurance(self, params):
        user_uuid = params.get('user_uuid', '')
        start_date = params.get('start_date', '')
        end_date = params.get('end_date', '')
        if not user_uuid:
            err = "user_uuid is required, params = " + str(params)
            LOG.info(err)
            raise exception.InvalidParamsException(err)
        if not start_date:
            err = "start_date is required, params = " + str(params)
            LOG.info(err)
            raise exception.InvalidParamsException(err)
        if not end_date:
            err = "end_date is required, params = " + str(params)
            LOG.info(err)
            raise exception.InvalidParamsException(err)
        name = params.get('name', '')
        insurance_type = params.get('insurance_type', '')
        description = params.get('description', '')
        insurance_period = params.get('insurance_period', '')
        money_per_period = params.get('money_per_period', 0)
        amount = params.get('amount', 0)
        excepted_income = params.get('excepted_income', 0)
        insurance = Insurance(
            user_uuid=user_uuid,
            name=name,
            start_date=start_date,
            end_date=end_date,
            description=description,
            insurance_type=insurance_type,
            insurance_period=insurance_period,
            money_per_period=money_per_period,
            amount=amount,
            excepted_income=excepted_income
        )
        DB.session.add(insurance)
        DB.session.commit()
        return self._make_insurance_dict(insurance)
 
    def update_insurance(self, id, params):
        try:
            insurance = DB.session.query(Insurance).filter_by(id=id).first()
            if not insurance:
                err = f'updating insurance {id} not exist'
                LOG.debug(err)
                raise exception.ObjectUpdateException(err)
            for key, value in params.items():
                setattr(insurance, key, value)
            DB.session.commit()
        except Exception as e:
            DB.session.rollback()
            DB.session.flush()
            err = f'updating insurance {id} error: {e}'
            LOG.debug(err)
            raise exception.ObjectUpdateException(err)
        return self._make_insurance_dict(insurance)

    def delete_insurance(self, id):
        insurance = DB.session.query(Insurance).filter_by(id=id).first()
        if not insurance:
            err = f'deleting insurance {id} not exist'
            LOG.debug(err)
            raise exception.ObjectDeleteException(err)
        try:
            DB.session.delete(insurance)
            DB.session.commit()
        except Exception as e:
            DB.session.rollback()
            DB.session.flush()
            err  = f'delete insurance {id} error: {e}'
            LOG.error(err)
            raise exception.ObjectDeleteException(err)

    def get_insurance(self, id):
        insurance = DB.session.query(Insurance).filter_by(id=id).first()
        if not insurance:
            raise exception.ObjectNotExistException(f'insurance {id} not exist')
        return self._make_insurance_dict(insurance)
    
    def list_insurances(self, filters):
        filter_conditions = []
        for key, value in filters.items():
            filter_conditions.append(getattr(Insurance, key) == value)
        try:
            insurances = DB.session.query(Insurance).filter(and_(*filter_conditions)).all()
        except Exception as e:
            raise exception.ObjectListException(f'list insurances error: {e}')
        return utils.convert_object_list(insurances)
