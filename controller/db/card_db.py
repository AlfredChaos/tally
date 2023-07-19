from cache import database, log
from common import exception
from controller.db import utils
from models.card import Card
from sqlalchemy import and_


LOG = log.get_global_log()
DB = database.get_global_db()


class CardDbMix():

    def _make_card_dict(self, obj):
        return utils.convert_dict(obj)

    def create_card(self, params):
        user_uuid = params.get('user_uuid', '')
        if not user_uuid:
            err = "user_uuid is required, params = " + str(params)
            LOG.info(err)
            raise exception.InvalidParamsException(err)
        name = params.get('name', '')
        bank = params.get('bank', '')
        card_type = params.get('card_type', '')
        fixed_deposit = params.get('fixed_deposit', 0)
        fixed_deposit_description = params.get('fixed_deposit_description', '')
        saving_deposit = params.get('saving_deposit', 0)
        saving_deposit_description = params.get('saving_deposit_description', '')
        card = Card(
            user_uuid=user_uuid,
            name=name,
            bank=bank,
            card_type=card_type,
            fixed_deposit=fixed_deposit,
            fixed_deposit_description=fixed_deposit_description,
            saving_deposit=saving_deposit,
            saving_deposit_description=saving_deposit_description
        )
        DB.session.add(card)
        DB.session.commit()
        return self._make_card_dict(card)

    def update_card(self, id, params):
        try:
            card = DB.session.query(Card).filter_by(id=id).first()
            if not card:
                err = f'updating card {id} not exist'
                LOG.debug(err)
                raise exception.ObjectUpdateException(err)
            for key, value in params.items():
                setattr(card, key, value)
            DB.session.commit()
        except Exception as e:
            DB.session.rollback()
            DB.session.flush()
            err = f'updating card {id} error: {e}'
            LOG.debug(err)
            raise exception.ObjectUpdateException(err)
        return self._make_card_dict(card)

    def delete_card(self, id):
        card = DB.session.query(Card).filter_by(id=id).first()
        if not card:
            err = f'deleting card {id} not exist'
            LOG.debug(err)
            raise exception.ObjectDeleteException(err)
        try:
            DB.session.delete(card)
            DB.session.commit()
        except Exception as e:
            DB.session.rollback()
            DB.session.flush()
            err  = f'delete card {id} error: {e}'
            LOG.error(err)
            raise exception.ObjectDeleteException(err)

    def get_card(self, id):
        card = DB.session.query(Card).filter_by(id=id).first()
        if not card:
            raise exception.ObjectNotExistException(f'card {id} not exist')
        return self._make_card_dict(card)

    def list_cards(self, filters):
        filter_conditions = []
        for key, value in filters.items():
            filter_conditions.append(getattr(Card, key) == value)
        try:
            cards = DB.session.query(Card).filter(and_(*filter_conditions)).all()
        except Exception as e:
            raise exception.ObjectListException(f'list cards error: {e}')
        return utils.convert_object_list(cards)