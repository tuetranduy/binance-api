import hashlib
import hmac
import time

import requests

import constants


def check_connectivity():
    response = requests.get(constants.REST_BASE_URL + '/fapi/v1/ping')

    if response.status_code == 200:
        print("Connection OK!")


def get_current_timestamp():
    return str(int(round(time.time() * 1000)) - 1000)


def create_signature(query):
    signature = hmac.new(constants.API_SECRET.encode(), msg=query.encode(), digestmod=hashlib.sha256).hexdigest()

    return signature
