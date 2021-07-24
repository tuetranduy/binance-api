import requests

from constants import constants
from utils import time_utils, signature_utils

query = 'symbol=ETHUSDT&timestamp=' + time_utils.get_current_timestamp()

headers = {'Content-Type': 'application/json', 'X-MBX-APIKEY': constants.API_KEY}
payload = {'symbol': 'ETHUSDT', 'timestamp': time_utils.get_current_timestamp(),
           'signature': signature_utils.create_signature(query)}

raw_response = requests.get(constants.REST_BASE_URL + '/fapi/v2/positionRisk', payload, headers=headers)

print(raw_response.json()[0])
