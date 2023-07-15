from sqlalchemy.orm import object_mapper, class_mapper

def convert_dict(object):
    result = []
    mapper = class_mapper(object.__class__)
    columns = [c.key for c in mapper.column_attrs]
    for column in columns:
        result[column] = getattr(object, column)
    return result