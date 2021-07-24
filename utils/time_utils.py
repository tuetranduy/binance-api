import time


def get_current_timestamp():
    return str(int(round(time.time() * 1000)) - 1000)
