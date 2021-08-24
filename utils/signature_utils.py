import hashlib
import hmac

from app.database import Database
from constants import constants

db = Database()


def create_signature(query):
    keys = db.get_keys()

    keys.secret_key = "" if keys.secret_key is None else keys.secret_key

    encoded_secret_key = keys.secret_key.encode() if constants.TEST_MODE is False else constants.API_SECRET.encode()

    signature = hmac.new(encoded_secret_key, msg=query.encode(), digestmod=hashlib.sha256).hexdigest()

    return signature
