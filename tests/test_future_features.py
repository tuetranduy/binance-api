from tests import client  # type: ignore


def test_get_position(client):
    data = client.get('/getPositions/BTCUSDT').get_json()
    assert 'data' in data
