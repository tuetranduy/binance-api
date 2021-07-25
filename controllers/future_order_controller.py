import requests

from constants import constants
from utils import param_builder


def get_all_opened_positions_by_symbol(symbol):
    headers = {'Content-Type': 'application/json', 'X-MBX-APIKEY': constants.API_KEY}
    query = {'symbol': symbol, 'timeInForce': 'GTC'}

    payload = param_builder.create_params_with_signature(query)

    response = requests.get(constants.REST_BASE_URL + '/fapi/v2/positionRisk', payload, headers=headers)

    return response.json()


def place_order(request):
    symbol = request.form['symbol']
    side = request.form['side']
    order_type = request.form['orderType']
    quantity = request.form['quantity']
    price = request.form['price']
    working_type = request.form['workingType']

    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'X-MBX-APIKEY': constants.API_KEY}
    query = {'symbol': symbol, 'side': side, 'type': order_type, 'quantity': quantity, 'price': price,
             'workingType': working_type, 'timeInForce': 'GTC'}

    payload = param_builder.create_params_with_signature(query)

    response = requests.post(constants.REST_BASE_URL + '/fapi/v1/order', payload, headers=headers)

    return response.json()


def place_hedge_order(request):
    symbol = request.form['symbol']
    side = request.form['side']
    position_side = request.form['positionSide']
    order_type = request.form['orderType']
    quantity = request.form['quantity']
    price = request.form['price']
    working_type = request.form['workingType']

    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'X-MBX-APIKEY': constants.API_KEY}
    query = {'symbol': symbol, 'side': side, 'positionSide': position_side, 'type': order_type, 'quantity': quantity,
             'price': price, 'workingType': working_type, 'timeInForce': 'GTC'}

    payload = param_builder.create_params_with_signature(query)

    response = requests.post(constants.REST_BASE_URL + '/fapi/v1/order', payload, headers=headers)

    return response.json()


def cancel_order(request):
    symbol = request.form['symbol']
    order_id = request.form['orderId']

    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'X-MBX-APIKEY': constants.API_KEY}
    query = {'symbol': symbol, 'orderId': order_id, 'timeInForce': 'GTC'}

    payload = param_builder.create_params_with_signature(query)

    response = requests.delete(constants.REST_BASE_URL + '/fapi/v1/order', data=payload, headers=headers)

    return response.json()


def cancel_all_opened_orders(request):
    symbol = request.form['symbol']

    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'X-MBX-APIKEY': constants.API_KEY}
    query = {'symbol': symbol, 'timeInForce': 'GTC'}

    payload = param_builder.create_params_with_signature(query)

    response = requests.delete(constants.REST_BASE_URL + '/fapi/v1/allOpenOrders', data=payload, headers=headers)

    return response.json()


def cancel_multiple_orders(request):
    symbol = request.form['symbol']
    order_id_list = request.form['orderIdList']

    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'X-MBX-APIKEY': constants.API_KEY}
    query = {'symbol': symbol, 'orderIdList': order_id_list, 'timeInForce': 'GTC'}

    payload = param_builder.create_params_with_signature(query)

    response = requests.delete(constants.REST_BASE_URL + '/fapi/v1/batchOrders', data=payload, headers=headers)

    return response.json()


# Close opened position for One-way order with MARKET_PRICE
def close_position_for_normal_order(request):
    symbol = request.form['symbol']
    side = request.form['side']
    order_type = request.form['type']
    quantity = request.form['quantity']
    working_type = request.form['workingType']

    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'X-MBX-APIKEY': constants.API_KEY}
    query = {'symbol': symbol, 'side': side, 'type': order_type, 'quantity': quantity, 'workingType': working_type}

    payload = param_builder.create_params_with_signature(query)

    response = requests.post(constants.REST_BASE_URL + '/fapi/v1/order', payload, headers=headers)

    return response.json()
