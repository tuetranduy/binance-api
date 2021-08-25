import hashlib
import hmac

from constants import constants


def create_signature(query, secret_key):
    secret_key = "" if secret_key is None else secret_key

    encoded_secret_key = secret_key.encode() if constants.TEST_MODE is False else constants.API_SECRET.encode()

    signature = hmac.new(encoded_secret_key, msg=query.encode(), digestmod=hashlib.sha256).hexdigest()

    return signature
