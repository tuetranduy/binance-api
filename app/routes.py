from flask import request

from app.server import app
from controllers import future_controller


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
