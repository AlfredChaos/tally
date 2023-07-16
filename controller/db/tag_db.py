from cache import database, log
from common import exception
from controller.db import utils
from models.tag import Tag
from sqlalchemy import and_


LOG = log.get_global_log()
DB = database.get_global_db()


class TagDbMix():

    def _make_tag_dict(self, obj):
        return utils.convert_dict(obj)

    def create_tag(self, params):
        user_uuid = params.get('user_uuid', '')
        if not user_uuid:
            err = "user_uuid is required, params = " + str(params)
            LOG.info(err)
            raise exception.InvalidParamsException(err)
        name = params.get('name', '')
        tag = Tag(
            user_uuid=user_uuid,
            name=name,
        )
        DB.session.add(tag)
        DB.session.commit()
        return self._make_tag_dict(tag)
 
    def update_tag(self, id, params):
        try:
            tag = DB.session.query(Tag).filter_by(id=id).first()
            if not tag:
                err = f'updating tag {id} not exist'
                LOG.debug(err)
                raise exception.ObjectUpdateException(err)
            for key, value in params.items():
                setattr(tag, key, value)
            DB.session.commit()
        except Exception as e:
            DB.session.rollback()
            DB.session.flush()
            err = f'updating tag {id} error: {e}'
            LOG.debug(err)
            raise exception.ObjectUpdateException(err)
        return self._make_tag_dict(tag)

    def delete_tag(self, id):
        tag = DB.session.query(Tag).filter_by(id=id).first()
        if not tag:
            err = f'deleting tag {id} not exist'
            LOG.debug(err)
            raise exception.ObjectDeleteException(err)
        try:
            DB.session.delete(tag)
            DB.session.commit()
        except Exception as e:
            DB.session.rollback()
            DB.session.flush()
            err  = f'delete tag {id} error: {e}'
            LOG.error(err)
            raise exception.ObjectDeleteException(err)

    def get_tag(self, id):
        tag = DB.session.query(Tag).filter_by(id=id).first()
        if not tag:
            raise exception.ObjectNotExistException(f'tag {id} not exist')
        return self._make_tag_dict(tag)
    
    def list_tags(self, filters):
        filter_conditions = []
        for key, value in filters.items():
            filter_conditions.append(getattr(Tag, key) == value)
        try:
            tags = DB.session.query(Tag).filter(and_(*filter_conditions)).all()
        except Exception as e:
            raise exception.ObjectListException(f'list tags error: {e}')
        return utils.convert_object_list(tags)


