from flask import request

from app.server import app
from controllers.api_controller import ApiController
from controllers.future_controller import FutureController
from controllers.socket_controller import SocketController

future_controller = FutureController()
socket_controller = SocketController()
api_controller = ApiController()


@app.post("/placeHedgeOrder")
def place_hedge_order():
    response = future_controller.place_future_order_hedge_mode(request)

    return response


@app.get("/getPositions/<symbol>")
def get_position(symbol):
    response = future_controller.get_position_by_symbol(symbol)

    return response


@app.delete("/cancelOrder")
def cancel_order():
    response = future_controller.cancel_order(request)

    return response


@app.delete("/cancelOrdersBySymbol")
def cancel_orders_by_symbol():
    response = future_controller.cancel_orders_by_symbol(request)

    return response


@app.delete("/cancelMultipleOrders")
def cancel_multiple_orders():
    response = future_controller.cancel_multiple_orders(request)

    return response


@app.post("/closePositionForOneWayOrder")
def close_position_for_normal_order():
    response = future_controller.close_position_for_normal_order(request)

    return response


@app.post("/closePositionForHedgeOrder")
def close_position_for_hedge_order():
    response = future_controller.close_position_for_hedge_order(request)

    return response


@app.post("/batchPositionForOneWayOrder")
def batch_close_position_for_normal_order():
    response = future_controller.batch_close_position_for_normal_order(request)

    return response


@app.get("/order")
def get_order():
    response = future_controller.get_order(request)

    return response


@app.get("/futureBalance")
def get_future_balance():
    response = future_controller.get_balance()

    return response


@app.post("/setTpAndSlForOpenedPosition")
def set_tp_and_sl():
    response = future_controller.set_tp_and_sl(request)

    return response


@app.get("/getListenKey")
def get_listen_key():
    response = socket_controller.get_listen_key()

    return response


@app.post("/setKeys")
def set_keys():
    response = api_controller.set_keys(request)

    return response


@app.get("/getKeys")
def get_keys():
    response = api_controller.get_keys()

    return response
