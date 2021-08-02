from binance.exceptions import BinanceAPIException

from core import ClientManager

client = ClientManager().init_client()


def get_listen_key():
    try:
        result = client.futures_stream_get_listen_key()

        return {
            'data': result
        }
    except BinanceAPIException as e:
        return {
                   'message': e.message,
                   'code': e.status_code
               }, e.status_code
