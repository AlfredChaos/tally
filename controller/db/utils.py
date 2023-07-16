from sqlalchemy.orm import object_mapper, class_mapper

def convert_dict(obj):
    result = {}
    mapper = class_mapper(obj.__class__)
    columns = [c.key for c in mapper.column_attrs]
    for column in columns:
        result[column] = getattr(obj, column)
        if column in ['created_at', 'updated_at']:
            result[column] = result[column].isoformat()
    return result


def convert_object_list(objs):
    result = []
    for obj in objs:
        res = convert_dict(obj)
        result.append(res)
    return result
