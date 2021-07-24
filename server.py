from flask import Flask

from future_order_controller import future_order

app = Flask(__name__, instance_relative_config=True)


@app.route("/getPosition/<position>")
def get_position_by_symbol(position):
    response = future_order.get_position_by_symbol(position)

    return {
        'data': response
    }
