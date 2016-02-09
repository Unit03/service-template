import pytest
import threading
import web
import tornado


@pytest.fixture(scope="session")
def running_app_base_url(request):

    port = 8888

    app = web.make_app()
    app.listen(port)

    def run_server():
        tornado.ioloop.IOLoop.instance().start()

    threading.Thread(target=run_server).start()

    def fin():
        tornado.ioloop.IOLoop.instance().stop()

    request.addfinalizer(fin)

    return "http://localhost:{}/".format(port)
