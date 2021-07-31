from binance.client import Client

from constants import constants


class ClientManager(object):

    @staticmethod
    def init_client():
        if constants.TEST_MODE:
            client = Client(constants.API_KEY, constants.API_SECRET, testnet=True)
            client.OPTIONS_TESTNET_URL = constants.REST_BASE_URL
        else:
            client = Client(constants.API_KEY, constants.API_SECRET, testnet=False)
        return client
