from flask import Flask, request

from controllers import future_order_controller

app = Flask(__name__, instance_relative_config=True)


@app.get("/getPositions/<position>")
def get_position(position):
    response = future_order_controller.get_all_opened_positions_by_symbol(position)

    return {
        'data': response
    }


@app.post("/placeOneWayOrder")
def place_one_way_order():
    response = future_order_controller.place_order(request)

    return {
        'data': response
    }


@app.post("/placeHedgeOrder")
def place_hedge_order():
    response = future_order_controller.place_hedge_order(request)

    return {
        'data': response
    }


@app.delete("/cancelOrder")
def cancel_order():
    response = future_order_controller.cancel_order(request)

    return {
        'data': response
    }


@app.delete("/cancelAllOrders")
def cancel_all_opened_orders():
    response = future_order_controller.cancel_all_opened_orders(request)

    return {
        'data': response
    }


@app.delete("/cancelMultipleOrders")
def cancel_multiple_orders():
    response = future_order_controller.cancel_multiple_orders(request)

    return {
        'data': response
    }
