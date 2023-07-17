from cache import database, log
from common import exception
from controller.db import utils
from controller.db._default_tag import default_tag
from models.tag import Tag, TagType, TagSource
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
        tag_type = params.get('tag_type', TagType.EXPAND)
        source = params.get('source', TagSource.DEFAULT)
        if name == 'default-not-exist':
            raise exception.InvalidParamsException(f'tag name {name} invalid')
        tag = Tag(
            user_uuid=user_uuid,
            name=name,
            tag_type=tag_type,
            source=source
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
                if key == 'name' and value == 'default-not-exist':
                    raise exception.InvalidParamsException(f'tag name {value} invalid')
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
        user_uuid = tag.user_uuid
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
        # 出于维护默认tag的需要
        # 当用户删除所有默认tag，创建一个标记
        filters = {'user_uuid': user_uuid, 'source': TagSource.DEFAULT}
        default_tags = self.list_tags(filters)
        if len(default_tags) == 0:
            params = {
                'name': 'default-not-exist',
                'tag_type': TagType.ANY,
                'source': TagSource.DEFAULT
            }
            dne = self.create_tag(params)
            LOG.info(f'default-not-exist created succeed: {dne}')

    def get_tag(self, id):
        tag = DB.session.query(Tag).filter_by(id=id).first()
        if not tag:
            raise exception.ObjectNotExistException(f'tag {id} not exist')
        return self._make_tag_dict(tag)
    
    def _list_tags(self, filters):
        filter_conditions = []
        for key, value in filters.items():
            filter_conditions.append(getattr(Tag, key) == value)
        try:
            tags = DB.session.query(Tag).filter(and_(*filter_conditions)).all()
        except Exception as e:
            raise exception.ObjectListException(f'list tags error: {e}')
        return utils.convert_object_list(tags)
    
    # 若不存在source=default的tag，则为用户创建所有默认tag
    # 过滤name=default-not-exist的tag，此tag仅为标记
    def list_tags(self, filters):
        user_uuid = filters.get('user_uuid', '')
        default_filter = {"source": TagSource.DEFAULT, 'user_uuid': user_uuid}
        default_tags = self._list_tags(default_filter)
        if len(default_tags) != 0:
            return self._list_tags(filters)
        for tag_type, tag_list in default_tag.items():
            for name in tag_list:
                params = {
                    "user_uuid": user_uuid,
                    "name": name,
                    "tag_type": tag_type,
                    "source": TagSource.DEFAULT
                }
                self.create_tag(params)
        return self._list_tags(filters)


