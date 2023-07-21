from cache import database, log
from common import exception
from controller.db import utils
from models.stock import Stock
from sqlalchemy import and_


LOG = log.get_global_log()
DB = database.get_global_db()


class StockDbMix():

    def _make_stock_dict(self, obj):
        return utils.convert_dict(obj)

    def create_stock(self, params):
        user_uuid = params.get('user_uuid', '')
        if not user_uuid:
            err = "user_uuid is required, params = " + str(params)
            LOG.info(err)
            raise exception.InvalidParamsException(err)
        name = params.get('name', '')
        money = params.get('money', 0)
        description = params.get('description', '')
        stock = Stock(
            user_uuid=user_uuid,
            name=name,
            money=money,
            description=description
        )
        DB.session.add(stock)
        DB.session.commit()
        return self._make_stock_dict(stock)

    def update_stock(self, id, params):
        try:
            stock = DB.session.query(Stock).filter_by(id=id).first()
            if not stock:
                err = f'updating stock {id} not exist'
                LOG.debug(err)
                raise exception.ObjectUpdateException(err)
            for key, value in params.items():
                setattr(stock, key, value)
            DB.session.commit()
        except Exception as e:
            DB.session.rollback()
            DB.session.flush()
            err = f'updating stock {id} error: {e}'
            LOG.debug(err)
            raise exception.ObjectUpdateException(err)
        return self._make_stock_dict(stock)

    def delete_stock(self, id):
        stock = DB.session.query(Stock).filter_by(id=id).first()
        if not stock:
            err = f'deleting stock {id} not exist'
            LOG.debug(err)
            raise exception.ObjectDeleteException(err)
        try:
            DB.session.delete(stock)
            DB.session.commit()
        except Exception as e:
            DB.session.rollback()
            DB.session.flush()
            err  = f'delete stock {id} error: {e}'
            LOG.error(err)
            raise exception.ObjectDeleteException(err)

    def get_stock(self, id):
        stock = DB.session.query(Stock).filter_by(id=id).first()
        if not stock:
            raise exception.ObjectNotExistException(f'stock {id} not exist')
        return self._make_stock_dict(stock)

    def list_stocks(self, filters):
        filter_conditions = []
        for key, value in filters.items():
            filter_conditions.append(getattr(Stock, key) == value)
        try:
            stocks = DB.session.query(Stock).filter(and_(*filter_conditions)).all()
        except Exception as e:
            raise exception.ObjectListException(f'list stocks error: {e}')
        return utils.convert_object_list(stocks)