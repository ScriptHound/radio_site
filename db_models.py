from ming import schema
from ming.odm import FieldProperty
from ming.odm.declarative import MappedClass

from db_creds import session


class Post(MappedClass):
    class __mongometa__:
        session = session
        name = 'posts'

    _id = FieldProperty(schema.ObjectId)
    title = FieldProperty(schema.String(required=True))
    text = FieldProperty(schema.String(required=True))
