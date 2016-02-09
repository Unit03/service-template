import tornado

from app.model.model import User


class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, from {}".format(User('Bob').say_name()))
