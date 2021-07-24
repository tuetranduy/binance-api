import hashlib
import hmac

from constants import constants


def create_signature(query):
    signature = hmac.new(constants.API_SECRET.encode(), msg=query.encode(), digestmod=hashlib.sha256).hexdigest()

    return signature
