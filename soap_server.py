from spyne import Application, ServiceBase, Unicode, rpc, Decimal
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication


class ExampleService(ServiceBase):

    @rpc(Decimal, Decimal, _returns=Decimal)
    def summa(ctx, x, y):
        return x + y

    @rpc(Decimal, Decimal, _returns=Decimal)
    def difference(ctx, a, b):
        return a - b


application = Application(
    services=[ExampleService],
    tns="http://tests.python-zeep.org/",
    in_protocol=Soap11(validator="lxml"),
    out_protocol=Soap11())

application = WsgiApplication(application)

if __name__ == "__main__":
    import logging

    from wsgiref.simple_server import make_server

    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger("spyne.protocol.xml").setLevel(logging.INFO)

    logging.info("listening to http://127.0.0.1:8000")
    logging.info("wsdl is at: http://localhost:8000/?wsdl")

    server = make_server("0.0.0.0", 8000, application)
    server.serve_forever()
