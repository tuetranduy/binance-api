import urllib

import requests

from constants import constants
from utils import time_utils, signature_utils


def get_position_by_symbol(symbol):
    headers = {'Content-Type': 'application/json', 'X-MBX-APIKEY': constants.API_KEY}
    query = {'symbol': symbol, 'timestamp': time_utils.get_current_timestamp()}

    print(urllib.parse.urlencode(query))

    signature = {'signature': signature_utils.create_signature(urllib.parse.urlencode(query))}

    payload = dict(query)
    payload.update(signature)

    response = requests.get(constants.REST_BASE_URL + '/fapi/v2/positionRisk', payload, headers=headers)

    return response.json()


def place_future_order(symbol, side, order_type, quantity, price, working_type):
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'X-MBX-APIKEY': constants.API_KEY}
    query = {'symbol': symbol, 'side': side, 'type': order_type, 'timeInForce': 'GTC', 'quantity': quantity,
             'price': price,
             'workingType': working_type, 'timestamp': time_utils.get_current_timestamp()}
    signature = {'signature': signature_utils.create_signature(urllib.parse.urlencode(query))}

    payload = dict(query)
    payload.update(signature)

    response = requests.post(constants.REST_BASE_URL + '/fapi/v1/order', payload, headers=headers)

    return response.json()


result = get_position_by_symbol('ETHUSDT')
print(result)

result2 = place_future_order('BTCUSDT', 'BUY', 'LIMIT', 5, 23456.67, 'MARK_PRICE')
print(result2)
