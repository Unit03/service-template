import tornado.ioloop
import tornado.web

from app.handlers.hello_handler import HelloHandler


def make_app():
    return tornado.web.Application([
        (r"/", HelloHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

