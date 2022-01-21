from wsgiref.simple_server import make_server
from spyne.server.wsgi import WsgiApplication

from SoapElectricCars import app


if __name__ == "__main__":
    wsgi_application = WsgiApplication(app)

    server = make_server('127.0.0.1', 8000, wsgi_application)
    server.serve_forever()
