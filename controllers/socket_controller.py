import time

from binance.exceptions import BinanceAPIException

from app.server import app
from core import ClientManager

client = ClientManager().init_client()

start_time = 0
expired_time = 0
key = ''


def get_listen_key():
    try:
        result = client.futures_stream_get_listen_key()

        global start_time
        global key
        key = result
        start_time = time.time()

        app.logger.debug(f'Listen key {key} created at timestamp: {start_time}')

        return {
            'data': result
        }
    except BinanceAPIException as e:
        return {
                   'msg': e.message,
                   'code': e.status_code
               }, e.status_code
