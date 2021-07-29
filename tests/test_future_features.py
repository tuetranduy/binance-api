from tests import client  # type: ignore


def test_get_position(client):
    data = client.get('/getPositions/BTCUSDT').get_json()
    assert 'data' in data


def test_get_order(client):
    data = client.get('/order', query_string=dict(symbol='BCHUSDT', orderId='769000069')).get_json()
    assert 'data' in data
