from flask import request

from app.server import app
from controllers import future_controller


@app.get("/getPositions/<position>")
def get_position(position):
    response = future_controller.get_all_opened_positions_by_symbol(position)

    return {
        'data': response
    }


@app.post("/placeOneWayOrder")
def place_one_way_order():
    response = future_controller.place_order(request)

    return {
        'data': response
    }


@app.post("/placeHedgeOrder")
def place_hedge_order():
    response = future_controller.place_hedge_order(request)

    return {
        'data': response
    }


@app.delete("/cancelOrder")
def cancel_order():
    response = future_controller.cancel_order(request)

    return {
        'data': response
    }


@app.delete("/cancelAllOrders")
def cancel_all_opened_orders():
    response = future_controller.cancel_all_opened_orders(request)

    return {
        'data': response
    }


@app.delete("/cancelMultipleOrders")
def cancel_multiple_orders():
    response = future_controller.cancel_multiple_orders(request)

    return {
        'data': response
    }


@app.post("/closePositionForOneWayOrder")
def close_position_for_normal_order():
    response = future_controller.close_position_for_normal_order(request)

    return {
        'data': response
    }


@app.post("/batchPositionForOneWayOrder")
def batch_close_position_for_normal_order():
    response = future_controller.batch_close_position_for_normal_order(request)

    return {
        'data': response
    }


@app.get("/order")
def get_order():
    response = future_controller.get_order(request)

    return {
        'data': response
    }


@app.get("/futureBalance")
def get_future_balance():
    response = future_controller.get_balance()

    return {
        'data': response
    }


@app.post("/changePositionMode")
def change_position_mode():
    response = future_controller.change_position_mode(request)

    return {
        'data': response
    }


@app.get("/getPositionMode")
def get_position_mode():
    response = future_controller.get_position_mode()

    return {
        'data': response
    }