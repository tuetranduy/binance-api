import urllib

from utils import signature_utils, time_utils


def create_params_with_signature(query):
    if query is None:
        payload = {'timestamp': time_utils.get_current_timestamp()}
        signature = {'signature': signature_utils.create_signature(urllib.parse.urlencode(payload))}
        payload.update(signature)

        return payload

    payload = dict(query)
    payload.update({'timestamp': time_utils.get_current_timestamp()})
    signature = {'signature': signature_utils.create_signature(urllib.parse.urlencode(payload))}
    payload.update(signature)

    return payload
