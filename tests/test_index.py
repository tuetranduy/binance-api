from tests import client  # type: ignore


def test_index_page_should_return_404(client):
    index = client.get('/')
    assert index.status_code == 404
