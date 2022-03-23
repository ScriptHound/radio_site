import os

from ming import create_datastore
from ming.odm import ThreadLocalODMSession

from dotenv import load_dotenv


load_dotenv('.env')

MONGO_USER = os.getenv('MONGO_USER')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD')
MONGO_DATABASE = os.getenv('MONGO_DATABASE')
MONGO_PORT = os.getenv('MONGO_PORT')
MONGO_HOST = os.getenv('HOST')

session = ThreadLocalODMSession(
    bind=create_datastore(
        f'mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DATABASE}')
)
