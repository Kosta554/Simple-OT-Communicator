import unittest
from Server import Server

class TestServer(unittest.TestCase):
    def test_server_start(self):
        server = Server()
        result = server.start()
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
