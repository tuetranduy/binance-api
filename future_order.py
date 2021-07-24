import requests

import constants
import ultils
import json

query = 'symbol=ETHUSDT&timestamp=' + ultils.get_current_timestamp()

headers = {'Content-Type': 'application/json', 'X-MBX-APIKEY': constants.API_KEY}
payload = {'symbol': 'ETHUSDT', 'timestamp': ultils.get_current_timestamp(), 'signature': ultils.create_signature(query)}

response = requests.get(constants.REST_BASE_URL + '/fapi/v2/positionRisk', payload, headers=headers)

print(response.json()[0])