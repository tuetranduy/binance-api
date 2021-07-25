from flask import Flask, request

from controllers import future_order_controller

app = Flask(__name__, instance_relative_config=True)


@app.get("/getPosition/<position>")
def get_position(position):
    response = future_order_controller.get_position_by_symbol(position)

    return {
        'data': response
    }


@app.post("/placeFutureOrder")
def place_future_order():
    symbol = request.form['symbol']
    side = request.form['side']
    order_type = request.form['orderType']
    quantity = request.form['quantity']
    price = request.form['price']
    working_type = request.form['workingType']

    response = future_order_controller.place_future_order(symbol, side, order_type, quantity, price, working_type)

    return {
        'data': response
    }
