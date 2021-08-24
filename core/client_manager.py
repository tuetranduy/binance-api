from binance.client import Client

from app.database import Database
from app.server import app
from constants import constants

db = Database()


class ClientManager(object):

    @staticmethod
    def init_client():

        app.logger.debug("=== Creating database ===")
        db.create_database()

        app.logger.debug('=== Binance API is in TEST MODE? %s ===', constants.TEST_MODE)

        if constants.TEST_MODE is True:
            client = Client(constants.API_KEY, constants.API_SECRET, testnet=True)
            client.OPTIONS_TESTNET_URL = constants.REST_BASE_URL
        else:
            keys = db.get_keys()

            keys.api_key = "" if keys.api_key is None else keys.api_key
            keys.secret_key = "" if keys.secret_key is None else keys.secret_key

            app.logger.debug('api_key: %s', keys.api_key)
            app.logger.debug('secret_key: %s', keys.secret_key)
            client = Client(keys.api_key, keys.secret_key, testnet=False)
        return client
