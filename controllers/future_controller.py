import requests

from app.server import app
from constants import constants
from utils import param_builder


def get_all_opened_positions_by_symbol(symbol):
    headers = {'Content-Type': 'application/json', 'X-MBX-APIKEY': constants.API_KEY}
    query = {'symbol': symbol, 'timeInForce': 'GTC'}

    payload = param_builder.create_params_with_signature(query)

    responses = requests.get(constants.REST_BASE_URL + '/fapi/v2/positionRisk', payload, headers=headers).json()

    return responses


def place_order(request):
    app.logger.debug('place_order_Requested data: %s', request.form)

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

    print(f"Requested payload: {payload}")

    response = requests.post(constants.REST_BASE_URL + '/fapi/v1/order', payload, headers=headers)

    return response.json()


def place_hedge_order(request):
    app.logger.debug('place_hedge_order_Requested data: %s', request.form)

    query = {}
    order_type = request.form['orderType']

    if order_type == 'LIMIT':
        symbol = request.form['symbol']
        side = request.form['side']
        position_side = request.form['positionSide']
        quantity = request.form['quantity']
        price = request.form['price']

        query = {'symbol': symbol, 'side': side, 'positionSide': position_side, 'type': order_type,
                 'quantity': quantity, 'price': price, 'timeInForce': 'GTC'}

    elif order_type == "MARKET":
        symbol = request.form['symbol']
        side = request.form['side']
        position_side = request.form['positionSide']
        quantity = request.form['quantity']

        query = {'symbol': symbol, 'side': side, 'positionSide': position_side, 'type': order_type,
                 'quantity': quantity}

    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'X-MBX-APIKEY': constants.API_KEY}

    payload = param_builder.create_params_with_signature(query)

    app.logger.debug('place_hedge_order_Requested payload: %s', payload)

    response = requests.post(constants.REST_BASE_URL + '/fapi/v1/order', payload, headers=headers).json()

    print(f"place_hedge_order_Response: {response}")

    return response


def cancel_order(request):
    app.logger.debug('cancel_order_Requested payload: %s', request.form)

    symbol = request.form['symbol']
    order_id = request.form['orderId']

    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'X-MBX-APIKEY': constants.API_KEY}
    query = {'symbol': symbol, 'orderId': order_id, 'timeInForce': 'GTC'}

    payload = param_builder.create_params_with_signature(query)

    response = requests.delete(constants.REST_BASE_URL + '/fapi/v1/order', data=payload, headers=headers)

    return response.json()


def cancel_all_opened_orders(request):
    app.logger.debug('cancel_all_opened_orders_Requested payload: %s', request.form)
    symbol = request.form['symbol']

    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'X-MBX-APIKEY': constants.API_KEY}
    query = {'symbol': symbol, 'timeInForce': 'GTC'}

    payload = param_builder.create_params_with_signature(query)

    response = requests.delete(constants.REST_BASE_URL + '/fapi/v1/allOpenOrders', data=payload, headers=headers)

    return response.json()


def cancel_multiple_orders(request):
    app.logger.debug('cancel_multiple_orders_Requested payload: %s', request.form)

    symbol = request.form['symbol']
    order_id_list = request.form['orderIdList']

    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'X-MBX-APIKEY': constants.API_KEY}
    query = {'symbol': symbol, 'orderIdList': order_id_list, 'timeInForce': 'GTC'}

    payload = param_builder.create_params_with_signature(query)

    response = requests.delete(constants.REST_BASE_URL + '/fapi/v1/batchOrders', data=payload, headers=headers)

    return response.json()


# Close opened position for One-way order with MARKET_PRICE
def close_position_for_normal_order(request):
    app.logger.debug('cancel_multiple_orders_Requested payload: %s', request.form)

    symbol = request.form['symbol']
    side = request.form['side']
    order_type = 'MARKET'
    quantity = request.form['quantity']
    working_type = request.form['workingType']

    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'X-MBX-APIKEY': constants.API_KEY}
    query = {'symbol': symbol, 'side': side, 'type': order_type, 'quantity': quantity, 'workingType': working_type}

    payload = param_builder.create_params_with_signature(query)

    response = requests.post(constants.REST_BASE_URL + '/fapi/v1/order', payload, headers=headers)

    return response.json()


# Batch close opened position for One-way order with MARKET_PRICE
def batch_close_position_for_normal_order(request):
    app.logger.debug('batch_close_position_for_normal_order_Requested payload: %s', request.get_json())

    positions = request.get_json()['data']

    response = []

    for position in positions:
        symbol = position['symbol']
        side = position['side']
        order_type = 'MARKET'
        quantity = position['quantity']
        working_type = position['workingType']

        headers = {'Content-Type': 'application/x-www-form-urlencoded', 'X-MBX-APIKEY': constants.API_KEY}
        query = {'symbol': symbol, 'side': side, 'type': order_type, 'quantity': quantity, 'workingType': working_type}

        payload = param_builder.create_params_with_signature(query)

        result = requests.post(constants.REST_BASE_URL + '/fapi/v1/order', payload, headers=headers).json()

        if 'code' in result:
            result['symbol'] = symbol

        response.append(result)

    return response


def get_order(request):
    app.logger.debug('get_order_Requested payload: %s', request.form)

    symbol = request.args.get('symbol')
    order_id = request.args.get('orderId')

    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'X-MBX-APIKEY': constants.API_KEY}
    query = {'symbol': symbol, 'orderId': order_id, 'timeInForce': 'GTC'}

    payload = param_builder.create_params_with_signature(query)

    response = requests.get(constants.REST_BASE_URL + '/fapi/v1/order', payload, headers=headers).json()

    return response


def get_balance():
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'X-MBX-APIKEY': constants.API_KEY}

    payload = param_builder.create_params_with_signature(None)

    response = requests.get(constants.REST_BASE_URL + '/fapi/v2/balance', payload, headers=headers).json()

    return response


def change_position_mode(request):
    dual_side_position = request.form['dualSidePosition']

    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'X-MBX-APIKEY': constants.API_KEY}
    query = {'dualSidePosition': dual_side_position}

    payload = param_builder.create_params_with_signature(query)

    response = requests.post(constants.REST_BASE_URL + '/fapi/v1/positionSide/dual', payload, headers=headers).json()

    return response


def get_position_mode():
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'X-MBX-APIKEY': constants.API_KEY}

    payload = param_builder.create_params_with_signature(None)

    response = requests.get(constants.REST_BASE_URL + '/fapi/v1/positionSide/dual', payload, headers=headers).json()

    return response


def set_tp_and_sl(request):
    app.logger.debug('set_tp_and_sl_Requested payload: %s', request.form)

    symbol = request.form['symbol']
    side = request.form['side']
    position_side = request.form['positionSide']
    quantity = request.form['quantity']
    order_type = request.form['orderType']
    stop_price = request.form['stopPrice']
    close_position = True

    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'X-MBX-APIKEY': constants.API_KEY}
    query = {'symbol': symbol, 'side': side, 'positionSide': position_side, 'type': order_type,
             'quantity': quantity, 'stopPrice': stop_price, 'closePosition': close_position, 'timeInForce': 'GTC'}

    payload = param_builder.create_params_with_signature(query)

    response = requests.post(constants.REST_BASE_URL + '/fapi/v1/order', payload, headers=headers).json()

    return response
