from binance.client import Client

from app.database import Database
from constants import constants

db = Database()


class ClientManager(object):

    @staticmethod
    def init_client():
        if constants.TEST_MODE:
            client = Client(constants.API_KEY, constants.API_SECRET, testnet=True)
            client.OPTIONS_TESTNET_URL = constants.REST_BASE_URL
        else:
            keys = db.get_keys()
            client = Client(keys.api_key, keys.secret_key, testnet=False)
        return client
