from binance.exceptions import BinanceAPIException

from app.server import app
from core import ClientManager

client = ClientManager().init_client()


def place_future_order_hedge_mode(request):
    app.logger.debug('place_hedge_order_Requested data: %s', request.form)

    order_type = request.form['orderType']
    result = {
        'code': 400,
        'message': 'Invalid order_type'
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
        return {
                   'message': e.message,
                   'code': e.status_code
               }, e.status_code


def get_position_by_symbol(symbol):
    try:
        result = client.futures_position_information(symbol=symbol)

        return {
            'data': result
        }

    except BinanceAPIException as e:
        return {
                   'message': e.message,
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
        return {
                   'message': e.message,
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
                   'message': e.message,
                   'code': e.status_code
               }, e.status_code


def cancel_multiple_orders(request):
    app.logger.debug('cancel_multiple_orders_Requested payload: %s', request.form)

    symbol = request.form['symbol']
    order_id_list = request.form['orderIdList']

    try:
        result = client.futures_cancel_orders(symbol=symbol, orderIdList=order_id_list)

        return {
            'data': result
        }

    except BinanceAPIException as e:
        return {
                   'message': e.message,
                   'code': e.status_code
               }, e.status_code


# Close opened position for One-way order with MARKET_PRICE
def close_position_for_normal_order(request):
    app.logger.debug('cancel_multiple_orders_Requested payload: %s', request.form)

    symbol = request.form['symbol']
    side = request.form['side']
    order_type = 'MARKET'
    quantity = request.form['quantity']

    try:
        result = client.futures_create_order(symbol=symbol, side=side, orderType=order_type, quantity=quantity)

        return {
            'data': result
        }

    except BinanceAPIException as e:
        return {
                   'message': e.message,
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
        result = client.futures_create_order(symbol=symbol, side=side, orderType=order_type, quantity=quantity,
                                             positionSide=position_side)

        return {
            'data': result
        }

    except BinanceAPIException as e:
        return {
                   'message': e.message,
                   'code': e.status_code
               }, e.status_code
