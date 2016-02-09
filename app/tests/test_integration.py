import requests


def test_fail(running_app_base_url):
    response = requests.get(running_app_base_url)
    assert response.text == 'Hello, from Bob'
