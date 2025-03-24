from twisted.trial import unittest
from twisted.internet import reactor, protocol
from twisted.test.proto_helpers import MemoryReactor

class EchoProtocol(protocol.Protocol):
    def dataReceived(self, data):
        self.transport.write(data)

class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return EchoProtocol()

class TestNetwork(unittest.TestCase):
    def setUp(self):
        self.reactor = MemoryReactor()
        self.factory = EchoFactory()
        self.port = self.reactor.listenTCP(0, self.factory)
        self.client = protocol.ClientCreator(self.reactor, protocol.Protocol)

    def test_echo(self):
        def gotProtocol(p):
            p.transport.write(b"hello")
            return p.dataReceived(b"hello")

        d = self.client.connectTCP("localhost", self.port.getHost().port)
        d.addCallback(gotProtocol)
        return d

if __name__ == "__main__":
    unittest.main()
