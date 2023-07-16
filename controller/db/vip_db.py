from cache import database, log
from common import exception
from controller.db import utils
from models.vip import Vip


LOG = log.get_global_log()
DB = database.get_global_db()


class VipDbMix():

    def _make_vip_dict(self, obj):
        return utils.convert_dict(obj)

    def create_vip(self, params):
        user_uuid = params.get('user_uuid', '')
        if not user_uuid:
            err = "user_uuid is required, params = " + str(params)
            LOG.info(err)
            raise exception.InvalidParamsException(err)
        name = params.get('name', '')
        fee = params.get('fee', 0)
        deduct_date = params.get('deduct_date', '')
        deduct_period = params.get('deduct_period', '')
        payment_channel = params.get('payment_channel', '')
        vip = Vip(
            user_uuid=user_uuid,
            name=name,
            fee=fee,
            deduct_date=deduct_date,
            deduct_period=deduct_period,
            payment_channel=payment_channel
        )
        DB.session.add(vip)
        DB.session.commit()
        return self._make_vip_dict(vip)
 
    def update_vip(self, id, params):
        try:
            vip = DB.session.query(Vip).filter_by(id=id).first()
            if not vip:
                err = f'updating vip {id} not exist'
                LOG.debug(err)
                raise exception.ObjectUpdateException(err)
            for key, value in params.items():
                setattr(vip, key, value)
            DB.session.commit()
        except Exception as e:
            DB.session.rollback()
            DB.session.flush()
            err = f'updating vip {id} error: {e}'
            LOG.debug(err)
            raise exception.ObjectUpdateException(err)
        return self._make_vip_dict(vip)

    def delete_vip(self, id):
        vip = DB.session.query(Vip).filter_by(id=id).first()
        if not vip:
            err = f'deleting vip {id} not exist'
            LOG.debug(err)
            raise exception.ObjectDeleteException(err)
        try:
            DB.session.delete(vip)
            DB.session.commit()
        except Exception as e:
            DB.session.rollback()
            DB.session.flush()
            err  = f'delete vip {id} error: {e}'
            LOG.error(err)
            raise exception.ObjectDeleteException(err)

    def get_vip(self, id):
        vip = DB.session.query(Vip).filter_by(id=id).first()
        if not vip:
            raise exception.ObjectNotExistException(f'vip {id} not exist')
        return self._make_vip_dict(vip)
