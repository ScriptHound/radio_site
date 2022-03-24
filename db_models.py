import typing

from ming import schema
from ming.odm import FieldProperty, MappedClass

from db_creds import session


if typing.TYPE_CHECKING:
    from ming.odm.mapper import Query


class Post(MappedClass):
    class __mongometa__:
        session = session
        name = 'posts'

    query: 'Query[Post]'

    _id = FieldProperty(schema.ObjectId)
    title = FieldProperty(schema.String(required=True))
    text = FieldProperty(schema.String(required=True))
