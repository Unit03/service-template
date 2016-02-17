import pytest
import threading
import web
import tornado


@pytest.fixture(scope="session")
def running_app_base_url(request):

    port = 8888

    web.make_app().listen(port)

    def run_server():
        tornado.ioloop.IOLoop.instance().start()

    def fin():
        tornado.ioloop.IOLoop.instance().stop()

    request.addfinalizer(fin)

    threading.Thread(target=run_server).start()

    return "http://localhost:{}/".format(port)
