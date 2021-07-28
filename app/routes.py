from flask import request
from sentry_sdk import capture_exception

from app.server import app
from controllers import future_controller


@app.get("/getPositions/<position>")
def get_position(position):
    try:
        response = future_controller.get_all_opened_positions_by_symbol(position)

        return {
            'data': response
        }

    except Exception as e:
        capture_exception(e)


@app.post("/placeOneWayOrder")
def place_one_way_order():
    try:
        response = future_controller.place_order(request)

        return {
            'data': response
        }

    except Exception as e:
        capture_exception(e)


@app.post("/placeHedgeOrder")
def place_hedge_order():
    try:
        response = future_controller.place_hedge_order(request)

        return {
            'data': response
        }

    except Exception as e:
        capture_exception(e)


@app.delete("/cancelOrder")
def cancel_order():
    try:
        response = future_controller.cancel_order(request)

        return {
            'data': response
        }

    except Exception as e:
        capture_exception(e)


@app.delete("/cancelAllOrders")
def cancel_all_opened_orders():
    try:
        response = future_controller.cancel_all_opened_orders(request)

        return {
            'data': response
        }

    except Exception as e:
        capture_exception(e)


@app.delete("/cancelMultipleOrders")
def cancel_multiple_orders():
    try:
        response = future_controller.cancel_multiple_orders(request)

        return {
            'data': response
        }

    except Exception as e:
        capture_exception(e)


@app.post("/closePositionForOneWayOrder")
def close_position_for_normal_order():
    try:
        response = future_controller.close_position_for_normal_order(request)

        return {
            'data': response
        }

    except Exception as e:
        capture_exception(e)


@app.post("/batchPositionForOneWayOrder")
def batch_close_position_for_normal_order():
    try:
        response = future_controller.batch_close_position_for_normal_order(request)

        return {
            'data': response
        }

    except Exception as e:
        capture_exception(e)


@app.get("/order")
def get_order():
    try:
        response = future_controller.get_order(request)

        return {
            'data': response
        }

    except Exception as e:
        capture_exception(e)


@app.get("/futureBalance")
def get_future_balance():
    try:
        response = future_controller.get_balance()

        return {
            'data': response
        }

    except Exception as e:
        capture_exception(e)


@app.post("/changePositionMode")
def change_position_mode():
    try:
        response = future_controller.change_position_mode(request)

        return {
            'data': response
        }

    except Exception as e:
        capture_exception(e)


@app.get("/getPositionMode")
def get_position_mode():
    try:
        response = future_controller.get_position_mode()

        return {
            'data': response
        }

    except Exception as e:
        capture_exception(e)
