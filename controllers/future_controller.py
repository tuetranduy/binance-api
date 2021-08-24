import requests
from binance.exceptions import BinanceAPIException

from app.database import Database
from app.server import app
from constants import constants
from core import ClientManager
from utils import param_builder

client = ClientManager().init_client()
db = Database()


def place_future_order_hedge_mode(request):
    app.logger.debug('place_hedge_order_Requested data: %s', request.form)

    order_type = request.form['orderType']
    result = {
        'code': 400,
        'msg': 'Invalid order_type'
    }

    try:
        if order_type == 'LIMIT':
            symbol = request.form['symbol']
            side = request.form['side']
            position_side = request.form['positionSide']
            quantity = request.form['quantity']
            price = request.form['price']

            result = client.futures_create_order(symbol=symbol,
                                                 side=side,
                                                 positionSide=position_side,
                                                 quantity=quantity,
                                                 price=price,
                                                 timeInForce='GTC',
                                                 type=order_type)
        elif order_type == "MARKET":
            symbol = request.form['symbol']
            side = request.form['side']
            position_side = request.form['positionSide']
            quantity = request.form['quantity']

            result = client.futures_create_order(symbol=symbol,
                                                 side=side,
                                                 positionSide=position_side,
                                                 quantity=quantity,
                                                 type=order_type)
        elif order_type == 'STOP':
            symbol = request.form['symbol']
            side = request.form['side']
            position_side = request.form['positionSide']
            quantity = request.form['quantity']
            price = request.form['price']
            stop_price = request.form['stopPrice']

            result = client.futures_create_order(symbol=symbol,
                                                 side=side,
                                                 positionSide=position_side,
                                                 quantity=quantity,
                                                 price=price,
                                                 stopPrice=stop_price,
                                                 type=order_type)
        return {
            'data': result
        }

    except BinanceAPIException as e:
        app.logger.debug('place_hedge_order_Exception: %s', e.message)
        return {
                   'msg': e.message,
                   'code': e.status_code
               }, e.status_code


def get_position_by_symbol(symbol):
    try:
        result = client.futures_position_information(symbol=symbol)

        return {
            'data': result
        }

    except BinanceAPIException as e:
        app.logger.debug('get_position_by_symbol_Exception: %s', e.message)
        return {
                   'msg': e.message,
                   'code': e.status_code
               }, e.status_code


def cancel_order(request):
    app.logger.debug('cancel_order_Requested payload: %s', request.form)

    symbol = request.form['symbol']
    order_id = request.form['orderId']

    try:
        result = client.futures_cancel_order(symbol=symbol, orderId=order_id)

        return {
            'data': result
        }

    except BinanceAPIException as e:
        app.logger.debug('cancel_order_Exception: %s', e.message)
        return {
                   'msg': e.message,
                   'code': e.status_code
               }, e.status_code


def cancel_orders_by_symbol(request):
    app.logger.debug('cancel_orders_Requested payload: %s', request.form)
    symbol = request.form['symbol']

    try:
        result = client.futures_cancel_all_open_orders(symbol=symbol)

        return {
            'data': result
        }

    except BinanceAPIException as e:
        return {
                   'msg': e.message,
                   'code': e.status_code
               }, e.status_code


# this controller using original binance api due to the fucking lib
def cancel_multiple_orders(request):
    app.logger.debug('cancel_multiple_orders_Requested payload: %s', request.form)

    keys = db.get_keys()

    keys.api_key = "" if keys.api_key is None else keys.api_key

    symbol = request.form['symbol']
    order_id_list = request.form['orderIdList']

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-MBX-APIKEY': keys.api_key if constants.TEST_MODE is False else constants.API_KEY
    }
    query = {'symbol': symbol, 'orderIdList': order_id_list, 'timeInForce': 'GTC'}

    payload = param_builder.create_params_with_signature(query)

    uri = constants.REST_BASE_URL_PROD if constants.TEST_MODE is False else constants.REST_BASE_URL

    response = requests.delete(
        uri + '/fapi/v1/batchOrders',
        data=payload,
        headers=headers
    )

    if response.status_code == 200:
        return {
            "data": response.json()
        }
    else:
        return response.json(), response.status_code


# Close opened position for One-way order with MARKET_PRICE
def close_position_for_normal_order(request):
    app.logger.debug('cancel_multiple_orders_Requested payload: %s', request.form)

    symbol = request.form['symbol']
    side = request.form['side']
    order_type = 'MARKET'
    quantity = request.form['quantity']

    try:
        result = client.futures_create_order(symbol=symbol, side=side, type=order_type, quantity=quantity)

        return {
            'data': result
        }

    except BinanceAPIException as e:
        return {
                   'msg': e.message,
                   'code': e.status_code
               }, e.status_code


# Close opened position for Hedge order with MARKET_PRICE
def close_position_for_hedge_order(request):
    app.logger.debug('close_position_for_hedge_order_Requested payload: %s', request.form)

    symbol = request.form['symbol']
    side = request.form['side']
    position_side = request.form['positionSide']
    order_type = 'MARKET'
    quantity = request.form['quantity']

    try:
        result = client.futures_create_order(symbol=symbol, side=side, type=order_type, quantity=quantity,
                                             positionSide=position_side)

        return {
            'data': result
        }

    except BinanceAPIException as e:
        app.logger.debug('close_position_for_hedge_order_Exception: %s', e.message)
        return {
                   'msg': e.message,
                   'code': e.status_code
               }, e.status_code


# Batch close opened position for One-way order with MARKET_PRICE
def batch_close_position_for_normal_order(request):
    app.logger.debug('batch_close_position_for_normal_order_Requested payload: %s', request.get_json())

    positions = request.get_json()['data']

    response = []

    try:
        for position in positions:
            symbol = position['symbol']
            side = position['side']
            order_type = 'MARKET'
            quantity = position['quantity']

            result = client.futures_create_order(symbol=symbol, side=side, type=order_type, quantity=quantity)

            if 'code' in result:
                result['symbol'] = symbol

            response.append(result)

        return {
            'data': response
        }

    except BinanceAPIException as e:
        return {
                   'msg': e.message,
                   'code': e.status_code
               }, e.status_code


def get_order(request):
    app.logger.debug('get_order_Requested payload: %s', request.form)

    symbol = request.args.get('symbol')
    order_id = request.args.get('orderId')

    try:
        response = client.futures_get_order(symbol=symbol, orderId=order_id)

        return {
            'data': response
        }

    except BinanceAPIException as e:
        return {
                   'msg': e.message,
                   'code': e.status_code
               }, e.status_code


def get_balance():
    try:
        response = client.futures_account_balance()

        return {
            'data': response
        }

    except BinanceAPIException as e:
        return {
                   'msg': e.message,
                   'code': e.status_code
               }, e.status_code


def set_tp_and_sl(request):
    symbol = request.form['symbol']
    side = request.form['side']
    position_side = request.form['positionSide']
    quantity = request.form['quantity']
    order_type = request.form['orderType']
    stop_price = request.form['stopPrice']

    response = {
        'code': 400,
        'msg': 'Invalid order_type'
    }

    try:
        if order_type == "TAKE_PROFIT_MARKET" or order_type == "STOP_MARKET":
            app.logger.debug('set_tp_and_sl: TAKE_PROFIT_MARKET')
            app.logger.debug('set_tp_and_sl_Requested payload: %s', request.form)
            response = client.futures_create_order(symbol=symbol, side=side, positionSide=position_side,
                                                   quantity=quantity,
                                                   type=order_type, stopPrice=stop_price, closePosition=True)

        elif order_type == "TAKE_PROFIT" or order_type == "STOP":
            app.logger.debug('set_tp_and_sl: TAKE_PROFIT')
            app.logger.debug('set_tp_and_sl_Requested payload: %s', request.form)
            price = request.form['price']
            response = client.futures_create_order(symbol=symbol, side=side, positionSide=position_side,
                                                   quantity=quantity, price=price,
                                                   type=order_type, stopPrice=stop_price)

        return {
            'data': response
        }

    except BinanceAPIException as e:
        app.logger.debug('set_tp_and_sl_Exception: %s', request.form)
        return {
                   'msg': e.message,
                   'code': e.status_code
               }, e.status_code
