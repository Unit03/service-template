import pytest
import tornado.web
from mock import patch

from app.handlers.hello_handler import HelloHandler
from app.model.model import User


@pytest.fixture
def app():
    return tornado.web.Application([
        (r'/', HelloHandler)
    ])


@pytest.mark.gen_test
def test_hello_handler(http_client, base_url):

    with patch.object(User, 'say_name', return_value='Jim'):
        response = yield http_client.fetch(base_url)
        assert response.body == "Hello, from Jim"
