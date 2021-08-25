import time

from binance.exceptions import BinanceAPIException

from app.server import app
from controllers.base_controller import BaseController


class SocketController(BaseController):
    start_time = 0
    expired_time = 0
    key = ''

    def get_listen_key(self):
        try:
            result = self.client.futures_stream_get_listen_key()

            self.key = result
            self.start_time = time.time()

            app.logger.debug(f'Listen key {self.key} created at timestamp: {self.start_time}')

            return {
                'data': result
            }
        except BinanceAPIException as e:
            return {
                       'msg': e.message,
                       'code': e.status_code
                   }, e.status_code
